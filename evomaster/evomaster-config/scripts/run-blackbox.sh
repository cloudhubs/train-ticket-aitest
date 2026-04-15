#!/bin/bash

# Script para executar EvoMaster em modo Black-Box
# Gera testes baseados em especificações OpenAPI/Swagger
# Suporta autenticação com diferentes roles (admin e user)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
CONFIG_DIR="$SCRIPT_DIR/../blackbox"
SWAGGER_DIR="$CONFIG_DIR/swagger-specs"
OUTPUT_DIR="${EVOMASTER_OUTPUT_DIR:-$PROJECT_ROOT/generated-tests/blackbox}"
TRAIN_TICKET_DIR="$PROJECT_ROOT/train-ticket-aitest"

# Carregar configuração de autenticação
if [ -f "$SCRIPT_DIR/auth-config.sh" ]; then
    source "$SCRIPT_DIR/auth-config.sh"
else
    echo -e "${YELLOW}AVISO: auth-config.sh não encontrado. Autenticação desabilitada.${NC}"
fi

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== EvoMaster Black-Box Test Generation ===${NC}\n"

# Verificar se Docker está disponível
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Erro: Docker não está instalado ou não está no PATH${NC}"
    exit 1
fi

# Verificar se os serviços estão rodando
echo -e "${YELLOW}Verificando se os serviços estão em execução...${NC}"
if ! curl -s -f http://localhost:8888/actuator/health &> /dev/null && ! curl -s -f http://localhost:8888/api/v1/auth/hello &> /dev/null; then
    echo -e "${YELLOW}Gateway não está respondendo. Iniciando serviços...${NC}"
    cd "$TRAIN_TICKET_DIR"
    if [ -f "docker-compose.yml" ]; then
        docker compose up -d consul mysql rabbitmq ts-new-gateway
        echo -e "${YELLOW}Aguardando serviços iniciarem (30 segundos)...${NC}"
        sleep 30
    else
        echo -e "${RED}Erro: docker-compose.yml não encontrado em $TRAIN_TICKET_DIR${NC}"
        exit 1
    fi
fi

# Extrair especificações Swagger se necessário
echo -e "\n${YELLOW}Extraindo especificações Swagger...${NC}"
if [ ! -d "$SWAGGER_DIR" ] || [ -z "$(ls -A "$SWAGGER_DIR"/*.json 2>/dev/null)" ]; then
    echo -e "${YELLOW}Nenhuma especificação encontrada. Executando extração...${NC}"
    bash "$SCRIPT_DIR/extract-swagger.sh"
else
    echo -e "${GREEN}Especificações Swagger já disponíveis${NC}"
fi

# Verificar se há especificações disponíveis
SWAGGER_FILES=$(find "$SWAGGER_DIR" -name "*.json" -o -name "*.yaml" -o -name "*.yml" 2>/dev/null | head -1)
if [ -z "$SWAGGER_FILES" ]; then
    echo -e "${RED}Erro: Nenhuma especificação Swagger/OpenAPI encontrada${NC}"
    echo -e "Execute primeiro: bash $SCRIPT_DIR/extract-swagger.sh"
    exit 1
fi

# Criar diretório de saída
mkdir -p "$OUTPUT_DIR"

# Configurar parâmetros do EvoMaster
MAX_TIME="${EVOMASTER_MAX_TIME:-1800}"  # 30 minutos padrão
RATE_PER_MINUTE="${EVOMASTER_RATE:-60}"
BASE_URL="${EVOMASTER_BASE_URL:-http://localhost:8888}"
TARGET_SERVICE="${1:-}"  # Primeiro argumento opcional: serviço específico
USER_ROLE="${2:-user}"   # Segundo argumento opcional: role (admin ou user)

# Validar role
if [ "$USER_ROLE" != "admin" ] && [ "$USER_ROLE" != "user" ]; then
    echo -e "${YELLOW}AVISO: Role inválida '$USER_ROLE'. Usando 'user' como padrão.${NC}"
    USER_ROLE="user"
fi

echo -e "\n${BLUE}Configuração:${NC}"
echo -e "  Tempo máximo: ${MAX_TIME}s"
echo -e "  Taxa: ${RATE_PER_MINUTE} req/min"
echo -e "  URL base: ${BASE_URL}"
echo -e "  Role: ${USER_ROLE}"
if [ -n "$TARGET_SERVICE" ]; then
    echo -e "  Serviço alvo: ${TARGET_SERVICE}"
fi

# Obter token de autenticação se auth-config.sh estiver disponível
AUTH_TOKEN=""
AUTH_HEADER=""
if [ -f "$SCRIPT_DIR/auth-config.sh" ]; then
    echo -e "\n${YELLOW}Obtendo token de autenticação para role: ${USER_ROLE}...${NC}"
    
    # Aguardar um pouco para garantir que o serviço de auth está pronto
    sleep 2
    
    if [ "$USER_ROLE" = "admin" ]; then
        AUTH_TOKEN=$(get_admin_token)
        if [ -n "$AUTH_TOKEN" ]; then
            AUTH_HEADER="Authorization: Bearer $AUTH_TOKEN"
            echo -e "${GREEN}✓ Token de admin obtido${NC}"
        else
            echo -e "${YELLOW}⚠ Não foi possível obter token de admin. Continuando sem autenticação.${NC}"
        fi
    else
        AUTH_TOKEN=$(get_user_token)
        if [ -n "$AUTH_TOKEN" ]; then
            AUTH_HEADER="Authorization: Bearer $AUTH_TOKEN"
            echo -e "${GREEN}✓ Token de usuário obtido${NC}"
        else
            echo -e "${YELLOW}⚠ Não foi possível obter token de usuário. Continuando sem autenticação.${NC}"
        fi
    fi
fi

# Determinar qual especificação usar
if [ -n "$TARGET_SERVICE" ]; then
    SPEC_FILE="$SWAGGER_DIR/${TARGET_SERVICE}-swagger.json"
    SPEC_FILE_NAME="${TARGET_SERVICE}-swagger.json"
    if [ ! -f "$SPEC_FILE" ]; then
        SPEC_FILE="$SWAGGER_DIR/${TARGET_SERVICE}-openapi.json"
        SPEC_FILE_NAME="${TARGET_SERVICE}-openapi.json"
    fi
    if [ ! -f "$SPEC_FILE" ]; then
        echo -e "${YELLOW}Especificação local não encontrada para '${TARGET_SERVICE}'${NC}"
        echo -e "${YELLOW}Arquivos disponíveis em $SWAGGER_DIR:${NC}"
        ls -1 "$SWAGGER_DIR"/*.{json,yaml,yml} 2>/dev/null | while read -r file; do
            echo -e "  - $(basename "$file")"
        done || echo -e "  (nenhum arquivo encontrado)"
        
        # Tentar usar gateway como fallback
        echo -e "\n${YELLOW}Tentando usar especificação do gateway...${NC}"
        GATEWAY_SPEC_URL="${BASE_URL}/v2/api-docs"
        if curl -s -f "$GATEWAY_SPEC_URL" &> /dev/null; then
            SWAGGER_URL="$GATEWAY_SPEC_URL"
            echo -e "${GREEN}✓ Usando especificação do gateway${NC}"
        else
            echo -e "${RED}✗ Gateway também não está acessível${NC}"
            echo -e "\n${YELLOW}Você pode:${NC}"
            echo -e "  1. Executar sem especificar serviço: ./run-blackbox.sh \"\" ${USER_ROLE}"
            echo -e "  2. Extrair a especificação do serviço em execução"
            echo -e "  3. Usar um dos serviços disponíveis listados acima"
            exit 1
        fi
    else
        # Usar caminho dentro do container Docker
        SWAGGER_URL="file:///swagger_specs/$SPEC_FILE_NAME"
    fi
else
    # Usar a primeira especificação encontrada ou gateway
    SWAGGER_URL="${BASE_URL}/v2/api-docs"
    if [ -n "$SWAGGER_FILES" ]; then
        FIRST_SPEC=$(ls -1 "$SWAGGER_DIR"/*.json 2>/dev/null | head -1)
        if [ -n "$FIRST_SPEC" ]; then
            SPEC_FILE_NAME=$(basename "$FIRST_SPEC")
            SWAGGER_URL="file:///swagger_specs/$SPEC_FILE_NAME"
        fi
    fi
fi

echo -e "  Especificação: ${SWAGGER_URL}"

# Executar EvoMaster via Docker
echo -e "\n${GREEN}Executando EvoMaster...${NC}"

# Preparar comando do Docker
DOCKER_CMD="docker run --rm \
    -v \"$OUTPUT_DIR\":/generated_tests \
    -v \"$SWAGGER_DIR\":/swagger_specs \
    --network host \
    webfuzzing/evomaster \
    --blackBox true \
    --bbSwaggerUrl \"$SWAGGER_URL\" \
    --maxTime \"${MAX_TIME}s\" \
    --ratePerMinute \"$RATE_PER_MINUTE\" \
    --outputFormat JAVA_JUNIT_5 \
    --outputFolder /generated_tests \
    --testSuiteFileName \"EvoMasterTest_${USER_ROLE}\""

# Adicionar header de autenticação se disponível
if [ -n "$AUTH_HEADER" ]; then
    # EvoMaster suporta headers customizados via --header
    # Formato: --header "HeaderName: HeaderValue"
    DOCKER_CMD="$DOCKER_CMD --header \"$AUTH_HEADER\""
    echo -e "${BLUE}Usando autenticação: ${USER_ROLE}${NC}"
fi

# Executar comando
eval $DOCKER_CMD

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo -e "\n${GREEN}✓ Testes gerados com sucesso!${NC}"
    echo -e "${GREEN}Localização: ${OUTPUT_DIR}${NC}"
    
    # Listar arquivos gerados
    if [ -d "$OUTPUT_DIR" ]; then
        echo -e "\n${BLUE}Arquivos gerados:${NC}"
        find "$OUTPUT_DIR" -type f -name "*.java" | head -10 | while read -r file; do
            echo -e "  - $(basename "$file")"
        done
    fi
else
    echo -e "\n${RED}✗ Erro ao executar EvoMaster (código: $EXIT_CODE)${NC}"
    exit $EXIT_CODE
fi

