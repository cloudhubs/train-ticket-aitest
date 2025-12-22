#!/bin/bash

# Configuração de credenciais para autenticação no EvoMaster
# Este arquivo contém as credenciais dos usuários admin e user

# ============================================
# CREDENCIAIS DE USUÁRIOS
# ============================================

# Usuário Administrador
export ADMIN_USERNAME="admin"
export ADMIN_PASSWORD="222222"
export ADMIN_ROLE="ROLE_ADMIN"

# Usuário Regular
export USER_USERNAME="fdse_microservice"
export USER_PASSWORD="111111"
export USER_ROLE="ROLE_USER"

# ============================================
# CONFIGURAÇÕES DE AUTENTICAÇÃO
# ============================================

# URL base do serviço de autenticação
export AUTH_SERVICE_URL="${AUTH_SERVICE_URL:-http://localhost:8890}"
export AUTH_LOGIN_ENDPOINT="${AUTH_SERVICE_URL}/api/v1/users/login"

# Gateway (se os serviços estiverem atrás de um gateway)
export GATEWAY_URL="${GATEWAY_URL:-http://localhost:8888}"
export GATEWAY_AUTH_ENDPOINT="${GATEWAY_URL}/api/v1/users/login"

# ============================================
# FUNÇÕES DE AUTENTICAÇÃO
# ============================================

# Função para obter token JWT para um usuário
# Uso: get_auth_token <username> <password> [auth_url]
# Retorna: token JWT ou string vazia em caso de erro
get_auth_token() {
    local username="$1"
    local password="$2"
    local auth_url="${3:-$AUTH_LOGIN_ENDPOINT}"
    
    if [ -z "$username" ] || [ -z "$password" ]; then
        echo "" >&2
        return 1
    fi
    
    # Tentar fazer login e extrair o token
    local response=$(curl -s -X POST "$auth_url" \
        -H "Content-Type: application/json" \
        -d "{\"username\":\"$username\",\"password\":\"$password\"}")
    
    # Verificar se a resposta contém um token
    # A resposta esperada é: {"status":1,"msg":"login success","data":{"userId":"...","username":"...","token":"..."}}
    local token=$(echo "$response" | grep -o '"token":"[^"]*"' | cut -d'"' -f4)
    
    if [ -z "$token" ]; then
        # Tentar via gateway se a primeira tentativa falhou
        if [ "$auth_url" != "$GATEWAY_AUTH_ENDPOINT" ]; then
            token=$(get_auth_token "$username" "$password" "$GATEWAY_AUTH_ENDPOINT")
        fi
    fi
    
    echo "$token"
}

# Função para obter token do admin
get_admin_token() {
    get_auth_token "$ADMIN_USERNAME" "$ADMIN_PASSWORD" "$1"
}

# Função para obter token do usuário regular
get_user_token() {
    get_auth_token "$USER_USERNAME" "$USER_PASSWORD" "$1"
}

# Função para verificar se um token é válido
# Uso: verify_token <token> [api_url]
verify_token() {
    local token="$1"
    local api_url="${2:-$GATEWAY_URL}"
    
    if [ -z "$token" ]; then
        return 1
    fi
    
    # Tentar fazer uma requisição autenticada
    local response=$(curl -s -o /dev/null -w "%{http_code}" \
        -H "Authorization: Bearer $token" \
        "${api_url}/api/v1/users/hello")
    
    [ "$response" = "200" ] || [ "$response" = "401" ]
}

# Função para exportar tokens como variáveis de ambiente
# Uso: export_auth_tokens [auth_url]
export_auth_tokens() {
    local auth_url="${1:-$AUTH_LOGIN_ENDPOINT}"
    
    echo "Obtendo tokens de autenticação..."
    
    export ADMIN_TOKEN=$(get_admin_token "$auth_url")
    export USER_TOKEN=$(get_user_token "$auth_url")
    
    if [ -n "$ADMIN_TOKEN" ]; then
        echo "✓ Token de admin obtido com sucesso"
    else
        echo "✗ Falha ao obter token de admin"
    fi
    
    if [ -n "$USER_TOKEN" ]; then
        echo "✓ Token de usuário obtido com sucesso"
    else
        echo "✗ Falha ao obter token de usuário"
    fi
}

# ============================================
# CONFIGURAÇÃO PARA EVOMASTER
# ============================================

# EvoMaster pode usar autenticação de várias formas:
# 1. Via headers customizados (--header)
# 2. Via arquivo de configuração
# 3. Via variáveis de ambiente

# Função para gerar headers de autenticação para EvoMaster
# Uso: get_evomaster_auth_headers <role>
# Retorna: string com headers formatados para EvoMaster
get_evomaster_auth_headers() {
    local role="${1:-user}"  # admin ou user
    
    local token=""
    if [ "$role" = "admin" ]; then
        token="${ADMIN_TOKEN:-$(get_admin_token)}"
    else
        token="${USER_TOKEN:-$(get_user_token)}"
    fi
    
    if [ -z "$token" ]; then
        echo "" >&2
        return 1
    fi
    
    echo "Authorization: Bearer $token"
}

# Função para criar arquivo de configuração de autenticação para EvoMaster
# Uso: create_evomaster_auth_config <output_file> [role]
create_evomaster_auth_config() {
    local output_file="$1"
    local role="${2:-user}"
    
    local token=""
    if [ "$role" = "admin" ]; then
        token="${ADMIN_TOKEN:-$(get_admin_token)}"
    else
        token="${USER_TOKEN:-$(get_user_token)}"
    fi
    
    if [ -z "$token" ]; then
        echo "Erro: Não foi possível obter token para role $role" >&2
        return 1
    fi
    
    # Criar arquivo JSON com configuração de autenticação
    cat > "$output_file" <<EOF
{
  "authentication": {
    "type": "bearer",
    "token": "$token",
    "header": "Authorization"
  },
  "user": {
    "username": "$([ "$role" = "admin" ] && echo "$ADMIN_USERNAME" || echo "$USER_USERNAME")",
    "role": "$([ "$role" = "admin" ] && echo "$ADMIN_ROLE" || echo "$USER_ROLE")"
  }
}
EOF
    
    echo "$output_file"
}



