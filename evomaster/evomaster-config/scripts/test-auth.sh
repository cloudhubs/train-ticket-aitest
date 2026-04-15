#!/bin/bash

# Script para testar autenticação e obter tokens
# Útil para verificar se as credenciais estão corretas antes de executar o EvoMaster

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Carregar configuração de autenticação
if [ ! -f "$SCRIPT_DIR/auth-config.sh" ]; then
    echo "Erro: auth-config.sh não encontrado em $SCRIPT_DIR"
    exit 1
fi

source "$SCRIPT_DIR/auth-config.sh"

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}=== Teste de Autenticação ===${NC}\n"

# Verificar se curl está disponível
if ! command -v curl &> /dev/null; then
    echo -e "${RED}Erro: curl não está instalado${NC}"
    exit 1
fi

# Verificar se o serviço de autenticação está acessível
echo -e "${YELLOW}Verificando conectividade com serviço de autenticação...${NC}"
if ! curl -s -f "${AUTH_SERVICE_URL}/api/v1/users/hello" &> /dev/null; then
    echo -e "${YELLOW}Tentando via gateway...${NC}"
    if ! curl -s -f "${GATEWAY_URL}/api/v1/users/hello" &> /dev/null; then
        echo -e "${RED}Erro: Serviço de autenticação não está acessível${NC}"
        echo -e "  Tentado: ${AUTH_SERVICE_URL}"
        echo -e "  Tentado: ${GATEWAY_URL}"
        exit 1
    else
        AUTH_URL="${GATEWAY_AUTH_ENDPOINT}"
        echo -e "${GREEN}✓ Gateway acessível${NC}"
    fi
else
    AUTH_URL="${AUTH_LOGIN_ENDPOINT}"
    echo -e "${GREEN}✓ Serviço de autenticação acessível${NC}"
fi

echo ""

# Testar autenticação do admin
echo -e "${BLUE}Testando autenticação de ADMIN:${NC}"
echo -e "  Usuário: ${ADMIN_USERNAME}"
echo -e "  Endpoint: ${AUTH_URL}"

ADMIN_TOKEN=$(get_admin_token "$AUTH_URL")

if [ -n "$ADMIN_TOKEN" ]; then
    echo -e "${GREEN}✓ Token obtido com sucesso${NC}"
    echo -e "  Token: ${ADMIN_TOKEN:0:50}..."
    
    # Verificar se o token é válido
    if verify_token "$ADMIN_TOKEN"; then
        echo -e "${GREEN}✓ Token válido${NC}"
    else
        echo -e "${YELLOW}⚠ Token pode ser inválido${NC}"
    fi
else
    echo -e "${RED}✗ Falha ao obter token${NC}"
fi

echo ""

# Testar autenticação do usuário regular
echo -e "${BLUE}Testando autenticação de USER:${NC}"
echo -e "  Usuário: ${USER_USERNAME}"
echo -e "  Endpoint: ${AUTH_URL}"

USER_TOKEN=$(get_user_token "$AUTH_URL")

if [ -n "$USER_TOKEN" ]; then
    echo -e "${GREEN}✓ Token obtido com sucesso${NC}"
    echo -e "  Token: ${USER_TOKEN:0:50}..."
    
    # Verificar se o token é válido
    if verify_token "$USER_TOKEN"; then
        echo -e "${GREEN}✓ Token válido${NC}"
    else
        echo -e "${YELLOW}⚠ Token pode ser inválido${NC}"
    fi
else
    echo -e "${RED}✗ Falha ao obter token${NC}"
fi

echo ""
echo -e "${BLUE}=== Resumo ===${NC}"
if [ -n "$ADMIN_TOKEN" ] && [ -n "$USER_TOKEN" ]; then
    echo -e "${GREEN}✓ Ambos os tokens foram obtidos com sucesso${NC}"
    echo -e "\nVocê pode usar os scripts do EvoMaster com autenticação:"
    echo -e "  ./run-blackbox.sh [serviço] [admin|user]"
    echo -e "  ./run-whitebox.sh [serviço] [admin|user]"
    exit 0
else
    echo -e "${RED}✗ Alguns tokens não foram obtidos${NC}"
    echo -e "\nVerifique:"
    echo -e "  1. Se os serviços estão rodando"
    echo -e "  2. Se as credenciais em auth-config.sh estão corretas"
    echo -e "  3. Se os usuários existem no banco de dados"
    exit 1
fi




