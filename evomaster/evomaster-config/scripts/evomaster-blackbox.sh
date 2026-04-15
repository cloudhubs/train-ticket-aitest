#!/bin/bash

# =============================================================================
# EvoMaster Black-Box Test Generator — Train Ticket
# =============================================================================
# Usage:
#   ./evomaster-blackbox.sh <service> [role]
#
# Examples:
#   ./evomaster-blackbox.sh ts-cancel-service admin
#   ./evomaster-blackbox.sh ts-contacts-service user
#   ./evomaster-blackbox.sh ts-preserve-service none
#
# Available services (must have a matching spec file in ../blackbox/swagger-specs/):
#   ts-admin-basic-service, ts-admin-order-service, ts-admin-user-service,
#   ts-assurance-service, ts-cancel-service, ts-contacts-service,
#   ts-inside-payment-service, ts-order-service, ts-preserve-service
#
# Available roles:
#   admin  — authenticated as ROLE_ADMIN (admin / 222222)
#   user   — authenticated as ROLE_USER  (fdse_microservice / 111111)
#   none   — no authentication
#
# Environment variables:
#   EVOMASTER_VERSION   EvoMaster version (default: 4.0.0)
#   EVOMASTER_IMAGE     Docker image override (default: webfuzzing/evomaster:v<VERSION>)
#   EVOMASTER_MAX_TIME  Max time in seconds (default: 60)
#   EVOMASTER_RATE      Requests per minute (default: 60)
#   EVOMASTER_SEED      Seed for reproducibility (default: random)
#   GATEWAY_URL         Base URL of the gateway (default: http://localhost:8888)
#   AUTH_SERVICE_URL    Direct URL to the auth service (default: http://localhost:8890)
# =============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPEC_DIR="$SCRIPT_DIR/../blackbox/swagger-specs"
OUTPUT_BASE_DIR="$SCRIPT_DIR/../generated-tests/blackbox"

# EvoMaster parameters
EVOMASTER_VERSION="${EVOMASTER_VERSION:-4.0.0}"
EVOMASTER_IMAGE="${EVOMASTER_IMAGE:-webfuzzing/evomaster:v${EVOMASTER_VERSION}}"
MAX_TIME="${EVOMASTER_MAX_TIME:-60}"
RATE_PER_MINUTE="${EVOMASTER_RATE:-60}"
SEED="${EVOMASTER_SEED:-}"

# Script arguments
SERVICE_NAME="${1:-}"
USER_ROLE="${2:-none}"

RUN_TIMESTAMP="$(date +%Y%m%d_%H%M%S)"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

# Load authentication configuration
source "$SCRIPT_DIR/auth-config.sh"

# =============================================================================
# Usage
# =============================================================================

show_usage() {
    echo -e "${BLUE}Usage:${NC} $0 <service> [role]"
    echo ""
    echo -e "${BLUE}Available services:${NC}"
    for f in "$SPEC_DIR"/*-openapi.json; do
        echo "  - $(basename "$f" -openapi.json)"
    done | sort
    echo ""
    echo -e "${BLUE}Roles:${NC}"
    echo -e "  admin  — ROLE_ADMIN (admin / 222222)"
    echo -e "  user   — ROLE_USER  (fdse_microservice / 111111)"
    echo -e "  none   — no authentication"
    echo ""
    echo -e "${BLUE}Environment variables:${NC}"
    echo -e "  EVOMASTER_VERSION   EvoMaster version (default: 4.0.0)"
    echo -e "  EVOMASTER_MAX_TIME  Max time in seconds (default: 60)"
    echo -e "  EVOMASTER_RATE      Requests per minute (default: 60)"
    echo -e "  EVOMASTER_SEED      Seed for reproducibility (default: random)"
}

# =============================================================================
# Validation
# =============================================================================

if [ -z "$SERVICE_NAME" ]; then
    echo -e "${RED}Error: service name is required${NC}\n"
    show_usage
    exit 1
fi

SPEC_FILE="$SPEC_DIR/${SERVICE_NAME}-openapi.json"
if [ ! -f "$SPEC_FILE" ]; then
    echo -e "${RED}Error: no spec file found for '${SERVICE_NAME}'${NC}"
    echo -e "${YELLOW}Expected: $SPEC_FILE${NC}\n"
    show_usage
    exit 1
fi

if [ "$USER_ROLE" != "admin" ] && [ "$USER_ROLE" != "user" ] && [ "$USER_ROLE" != "none" ]; then
    echo -e "${YELLOW}Warning: unknown role '${USER_ROLE}'. Using 'none'.${NC}"
    USER_ROLE="none"
fi

if ! command -v docker &>/dev/null; then
    echo -e "${RED}Error: Docker is not installed${NC}"
    exit 1
fi

# =============================================================================
# Output directory: <service>/<role>/
# =============================================================================

OUTPUT_DIR="$OUTPUT_BASE_DIR/$SERVICE_NAME/$USER_ROLE"
mkdir -p "$OUTPUT_DIR"

LOG_FILE="$OUTPUT_DIR/evomaster.log"

echo -e "${BLUE}=== EvoMaster Black-Box — Train Ticket ===${NC}\n"
echo -e "${YELLOW}Service:${NC}    $SERVICE_NAME"
echo -e "${YELLOW}Role:${NC}       $USER_ROLE"
echo -e "${YELLOW}Max time:${NC}   ${MAX_TIME}s"
echo -e "${YELLOW}Rate:${NC}       ${RATE_PER_MINUTE} req/min"
echo -e "${YELLOW}Timestamp:${NC}  $RUN_TIMESTAMP"
echo -e "${YELLOW}EvoMaster:${NC}  ${EVOMASTER_IMAGE}"
echo -e "${YELLOW}Spec:${NC}       $(basename "$SPEC_FILE")"
echo -e "${YELLOW}Output:${NC}     $OUTPUT_DIR"
if [ -n "$SEED" ]; then
    echo -e "${YELLOW}Seed:${NC}       $SEED"
fi
echo ""

# =============================================================================
# Check gateway reachability
# =============================================================================

echo -e "${YELLOW}Checking gateway at ${GATEWAY_URL}...${NC}"
GW_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "${GATEWAY_URL}" 2>/dev/null || echo "000")
if [ "$GW_STATUS" = "000" ]; then
    echo -e "${RED}✗ Gateway not reachable at ${GATEWAY_URL}${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Gateway reachable (HTTP ${GW_STATUS})${NC}"

# =============================================================================
# Authentication
# =============================================================================

AUTH_HEADER=""

if [ "$USER_ROLE" = "none" ]; then
    echo -e "\n${YELLOW}Running without authentication${NC}"
else
    echo -e "\n${YELLOW}Fetching JWT token for role '${USER_ROLE}'...${NC}"

    if [ "$USER_ROLE" = "admin" ]; then
        TOKEN=$(get_admin_token)
    else
        TOKEN=$(get_user_token)
    fi

    if [ -n "$TOKEN" ]; then
        echo -e "${GREEN}✓ Token obtained${NC}"
        AUTH_HEADER="Authorization:Bearer $TOKEN"
    else
        echo -e "${RED}✗ Failed to obtain token. Check that the auth service is running.${NC}"
        exit 1
    fi
fi

# =============================================================================
# Save run metadata
# =============================================================================

SEED_VALUE="${SEED:-random}"
cat > "$OUTPUT_DIR/run-info.json" <<EOF
{
  "service": "$SERVICE_NAME",
  "role": "$USER_ROLE",
  "timestamp": "$RUN_TIMESTAMP",
  "max_time_seconds": $MAX_TIME,
  "rate_per_minute": $RATE_PER_MINUTE,
  "seed": "$SEED_VALUE",
  "spec_file": "$(basename "$SPEC_FILE")",
  "gateway_url": "$GATEWAY_URL",
  "authenticated": $([ "$USER_ROLE" != "none" ] && echo "true" || echo "false"),
  "evomaster_version": "$EVOMASTER_VERSION",
  "evomaster_image": "$EVOMASTER_IMAGE"
}
EOF

echo -e "${GREEN}✓ Metadata saved to run-info.json${NC}"

# =============================================================================
# Run EvoMaster via Docker
# =============================================================================

TEST_SUITE_NAME="EvoMaster_${SERVICE_NAME}_${USER_ROLE}"

echo -e "\n${GREEN}Running EvoMaster...${NC}"
echo -e "${YELLOW}Log:${NC} $LOG_FILE"
echo ""

DOCKER_ARGS=(
    "run" "--rm"
    "--user" "$(id -u):$(id -g)"
    "--network" "host"
    "-v" "$OUTPUT_DIR:/output"
    "-v" "$SPEC_DIR:/swagger"
    "$EVOMASTER_IMAGE"
    "--blackBox" "true"
    "--bbSwaggerUrl" "file:///swagger/${SERVICE_NAME}-openapi.json"
    "--maxTime" "${MAX_TIME}s"
    "--ratePerMinute" "$RATE_PER_MINUTE"
    "--outputFormat" "JAVA_JUNIT_5"
    "--outputFolder" "/output"
    "--testSuiteFileName" "$TEST_SUITE_NAME"
    "--writeStatistics" "true"
    "--statisticsFile" "/output/statistics.csv"
    "--snapshotInterval" "1"
)

if [ -n "$SEED" ]; then
    DOCKER_ARGS+=("--seed" "$SEED")
fi

if [ -n "$AUTH_HEADER" ]; then
    DOCKER_ARGS+=("--header0" "$AUTH_HEADER")
    echo -e "${BLUE}Authentication header configured${NC}"
fi

docker "${DOCKER_ARGS[@]}" 2>&1 | tee "$LOG_FILE"
EXIT_CODE=${PIPESTATUS[0]}

# =============================================================================
# Extract summary from log and append to run-info.json
# =============================================================================

if [ -f "$LOG_FILE" ]; then
    COVERED=$(grep -oP "Covered targets: \K[0-9]+" "$LOG_FILE" | tail -1 || echo "unknown")
    ENDPOINTS_2XX=$(grep -oP "Successfully executed \(HTTP code 2xx\) \K[0-9]+ endpoints out of [0-9]+" "$LOG_FILE" | tail -1 || echo "unknown")
    TESTS_GENERATED=$(grep -oP "Going to save \K[0-9]+" "$LOG_FILE" | tail -1 || echo "unknown")

    TMP=$(mktemp)
    while IFS= read -r line || [ -n "$line" ]; do
        if [[ "$line" == *"\"evomaster_image\""* ]]; then
            printf '%s,\n' "$line"
            printf '%s\n' '  "results": {'
            printf '%s\n' "    \"covered_targets\": \"$COVERED\","
            printf '%s\n' "    \"endpoints_2xx\": \"$ENDPOINTS_2XX\","
            printf '%s\n' "    \"tests_generated\": \"$TESTS_GENERATED\","
            printf '%s\n' "    \"exit_code\": $EXIT_CODE"
            printf '%s\n' '  }'
        else
            printf '%s\n' "$line"
        fi
    done < "$OUTPUT_DIR/run-info.json" > "$TMP"
    mv "$TMP" "$OUTPUT_DIR/run-info.json"
fi

# =============================================================================
# Final result
# =============================================================================

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}✓ Tests generated successfully!${NC}"
    echo -e "${YELLOW}Location:${NC} $OUTPUT_DIR"
    echo ""
    echo -e "${BLUE}Generated files:${NC}"
    ls "$OUTPUT_DIR" | while read -r f; do
        echo "  - $f"
    done
else
    echo -e "${RED}✗ EvoMaster failed (exit code: $EXIT_CODE)${NC}"
    echo -e "${YELLOW}Full log at:${NC} $LOG_FILE"
    exit $EXIT_CODE
fi
