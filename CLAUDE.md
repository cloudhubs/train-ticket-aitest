# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Train Ticket is a microservices-based railway ticket booking system consisting of 22 Spring Boot services orchestrated via Docker Compose. The system uses Consul for service discovery, MySQL for data persistence, RabbitMQ for messaging, and Spring Cloud Gateway for API routing.

## Architecture

### Service Discovery & Communication
- **Consul** (port 8500): Service registry and discovery
- **Gateway**: `ts-new-gateway` (port 8888) - Spring Cloud Gateway routing all API traffic via `/api/v1/**` paths
- **Inter-service Communication**: Services use `RestTemplate` with `ServiceResolver` pattern to route through the gateway rather than direct service-to-service calls
- **Service Resolution**: Each service implements `ServiceResolverImpl` which maps logical service names to physical service names and routes through `http://ts-new-gateway:8888/`

### Security Architecture (RBAC Migration)
- Services are being migrated to configuration-based RBAC from hardcoded security rules
- **Authorization Configuration**: RBAC rules defined in `application.yml` under `security.authorization-rules`
- **Key Classes**:
  - `AuthorizationRule.java`: POJO for path/method/authority mappings
  - `SecurityProperties.java`: Configuration properties binding (`@ConfigurationProperties("security")`)
  - `WebSecurityConfig.java`: Dynamically applies rules from YAML to Spring Security filter chain
- **Current Migration Status** (branch `policy-config-migration`): Migrated services include auth, admin, assurance, cancel, config, consign, contacts, delivery, and food services
- **Pattern**: Each service defines its own authorization rules in its `application.yml`; rules support `permitAll`, `authenticated`, or specific roles (e.g., `ROLE_ADMIN`)

### JWT Authentication
- JWT tokens managed by `JWTFilter`, `JWTProvider`, and `JWTUtil` classes in each service's `config/jwt/` package
- Token validation occurs at individual service level via `JWTFilter` before `UsernamePasswordAuthenticationFilter`

### Data Architecture
- **MySQL** (port 3306): Each microservice has its own database schema (e.g., `ts-auth-service`, `ts-order-service`)
- **JPA/Hibernate**: `ddl-auto: update` for schema evolution
- **Connection Pool**: HikariCP with `maximum-pool-size: 2` (configurable per service)
- **Timestamp Convention**: Always use timestamp with timezone for time-related database fields

### Messaging
- **RabbitMQ** (port 5672, management UI 15672): Asynchronous communication
- Queue definitions in `config/Queues.java` classes

### Microservices Structure (22 services)
All services follow consistent Spring Boot structure:
```
ts-<service-name>/
├── src/main/java/com/cloudhubs/trainticket/<service>/
│   ├── config/           # Security, JWT, email, Swagger configs
│   │   ├── jwt/          # JWTFilter, JWTProvider, JWTUtil
│   │   ├── AuthorizationRule.java
│   │   ├── SecurityProperties.java
│   │   └── WebSecurityConfig.java
│   ├── controller/       # REST endpoints
│   ├── service/          # Business logic
│   │   └── impl/         # Service implementations + ServiceResolverImpl
│   ├── entity/           # JPA entities
│   ├── repository/       # Spring Data JPA repositories
│   ├── dto/              # Data transfer objects
│   └── util/             # Utility classes
├── src/main/resources/
│   └── application.yml   # Port, Consul, DB, RabbitMQ, RBAC config
├── Dockerfile            # Multi-stage: maven build + JRE runtime (optional telemetry stage)
└── pom.xml               # Spring Boot 3.2.1, Java 17, Spring Cloud 2023.0.0
```

**Key Services**:
- `ts-auth-service` (8890): Authentication, user management, token generation
- `ts-order-service` (8900): Order creation, ticket preservation
- `ts-preserve-service` (8901): Ticket reservation logic
- `ts-food-service` (8896): Food ordering
- `ts-admin-service` (8887): Admin operations
- `ts-config-service` (8892): Payment and user configuration
- `ts-user-service` (8908): User profile management
- And 15+ domain-specific services (travel, route, price, station, etc.)

### Gateway Routing Pattern
Services expose controllers at paths like `/api/v1/<logical-service-name>/**`, which the gateway routes to physical service instances via Consul service discovery using `lb://<physical-service-name>`.

Example: A request to `/api/v1/users/**` routes to `ts-auth-service`.

## Development Commands

### Building & Running

**Start full system**:
```bash
docker compose up --build -d
```

**Start with telemetry** (OpenTelemetry Java agent):
```bash
docker compose -f docker-compose.yml -f docker-compose.override.telemetry.yml up --build -d
```

**Build and deploy all services** (uses `build-deploy-services.sh`):
```bash
chmod +x build-deploy-services.sh
./build-deploy-services.sh
```
This script:
1. Iterates through all directories with Dockerfiles
2. Builds Docker images as `<service-name>:latest`
3. Waits 60 seconds for infrastructure services
4. Runs `docker-compose up -d`

**Stop services**:
```bash
docker compose down
```

**Check running services**:
```bash
docker ps
```

### Building Individual Services

Each service uses Maven (Java 17, Spring Boot 3.2.1):

**Build service**:
```bash
cd ts-<service-name>
mvn clean verify
```

**Skip tests**:
```bash
mvn clean verify -DskipTests
```

**Build Docker image manually**:
```bash
cd ts-<service-name>
docker build -t ts-<service-name>:latest .
```

**Run individual service** (requires Consul, MySQL, RabbitMQ running):
```bash
docker compose up -d consul mysql rabbitmq
docker compose up ts-<service-name>
```

### Testing

Run tests for a specific service:
```bash
cd ts-<service-name>
mvn test
```

Run single test class:
```bash
mvn test -Dtest=<TestClassName>
```

## Common Development Patterns

### Adding RBAC Configuration to a Service

When migrating a service to config-based RBAC:

1. **Add configuration properties classes**:
   - Create `AuthorizationRule.java` (if not exists)
   - Create `SecurityProperties.java` with `@ConfigurationProperties("security")`

2. **Update `WebSecurityConfig.java`**:
   - Add `@EnableConfigurationProperties(SecurityProperties.class)`
   - Inject `SecurityProperties`
   - Iterate over `securityProperties.getAuthorizationRules()` in `filterChain()` method
   - Apply rules dynamically using `HttpSecurity.authorizeHttpRequests()`

3. **Define rules in `application.yml`**:
   ```yaml
   security:
     authorization-rules:
       - paths: ["/api/v1/admin/**"]
         method: "GET"
         authorities: ["ROLE_ADMIN"]
       - paths: ["/api/v1/public/**"]
         authorities: ["permitAll"]
   ```

4. **Authority types**:
   - `permitAll`: Public access
   - `authenticated`: Any authenticated user
   - `ROLE_*`: Specific role (e.g., `ROLE_ADMIN`, `ROLE_USER`)

### Adding a New Service Dependency

When a service needs to call another service:

1. Use `ServiceResolver.getServiceUrl(String serviceName)` to get the gateway-routed URL
2. Inject `RestTemplate` and make HTTP calls to the resolved URL
3. Add the service mapping in `ServiceResolverImpl` if not present
4. Ensure gateway has routing rule in `ts-new-gateway/src/main/resources/application.yml`

### Environment Configuration

Services read environment variables from Docker Compose:
- `CONSUL_HOST`: Consul server hostname (default: `localhost`)
- `MYSQL_HOST`: MySQL server hostname (default: `localhost`)
- `RABBIT_HOST`: RabbitMQ server hostname (default: `localhost`)

Override defaults in `docker-compose.yml` or local runs via env vars.

## Technology Stack

- **Java**: 17
- **Spring Boot**: 3.2.1
- **Spring Cloud**: 2023.0.0 (Consul discovery, Gateway)
- **Spring Security**: JWT-based authentication, RBAC
- **Database**: MySQL 8.0.33 with JPA/Hibernate
- **Messaging**: Spring AMQP with RabbitMQ
- **Service Discovery**: Consul 1.15.4
- **API Gateway**: Spring Cloud Gateway (reactive)
- **Build Tool**: Maven 3.9.6
- **Container Runtime**: Docker, Docker Compose v2.26+
- **Telemetry** (optional): OpenTelemetry Java agent 2.3.0

## UI Access

- **UI Dashboard**: http://localhost:8080 (`ts-ui-service`)
- **API Gateway**: http://localhost:8888 (`ts-new-gateway`)
- **Consul UI**: http://localhost:8500
- **RabbitMQ Management**: http://localhost:15672 (guest/guest)

## Current Work

The `policy-config-migration` branch is actively migrating services from hardcoded Spring Security configurations to YAML-based RBAC rules. Pattern established in `ts-auth-service` and replicated across services. Reference commit `1eff1e2` for the auth service migration approach.
