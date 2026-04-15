#!/bin/bash

# Authentication configuration for EvoMaster on Train Ticket
# Train Ticket uses its own JWT-based authentication (POST /api/v1/users/login)

# ============================================
# ENDPOINTS
# ============================================

export AUTH_SERVICE_URL="${AUTH_SERVICE_URL:-http://localhost:8890}"
export GATEWAY_URL="${GATEWAY_URL:-http://localhost:8888}"

AUTH_LOGIN_PATH="/api/v1/users/login"

# ============================================
# USER CREDENTIALS
# ============================================

export ADMIN_USERNAME="${ADMIN_USERNAME:-admin}"
export ADMIN_PASSWORD="${ADMIN_PASSWORD:-222222}"

export USER_USERNAME="${USER_USERNAME:-fdse_microservice}"
export USER_PASSWORD="${USER_PASSWORD:-111111}"

# ============================================
# AUTHENTICATION FUNCTIONS
# ============================================

# Obtain a JWT token from the auth service.
# Tries the auth service directly first, then falls back to the gateway.
# Usage: get_token <username> <password>
get_token() {
    local username="$1"
    local password="$2"

    local payload="{\"username\":\"${username}\",\"password\":\"${password}\"}"

    for base_url in "$AUTH_SERVICE_URL" "$GATEWAY_URL"; do
        local response
        response=$(curl -s -X POST "${base_url}${AUTH_LOGIN_PATH}" \
            -H "Content-Type: application/json" \
            -d "$payload" 2>/dev/null)

        local token
        token=$(echo "$response" | grep -o '"token":"[^"]*"' | cut -d'"' -f4)

        if [ -n "$token" ]; then
            echo "$token"
            return 0
        fi
    done

    echo "Error: could not obtain token for '${username}'" >&2
    return 1
}

get_admin_token() {
    get_token "$ADMIN_USERNAME" "$ADMIN_PASSWORD"
}

get_user_token() {
    get_token "$USER_USERNAME" "$USER_PASSWORD"
}
