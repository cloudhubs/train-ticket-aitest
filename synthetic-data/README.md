# Synthetic Data — Train Ticket

Pre-generated synthetic seed data for the Train Ticket microservices benchmark (22 Spring Boot services).

## Output files

All artifacts are in `output/`:

| File | Description |
|------|-------------|
| `flow-graph.mmd` | Mermaid diagram of the service call graph |
| `flow-matrix.md` | ~155 API flows with role and data-state requirements |
| `scenarios.md` | 14 data-state groups × 50 scenarios each (700 scenarios) |
| `seed-all.sql` | MySQL `INSERT IGNORE` statements for all service databases |
| `setup-auth.sh` | Registers 50 test users via `POST /api/v1/users/register` |
| `postman_seed.json` | Postman 2.1 collection covering all flows |
| `docker-compose.test.yml` | MySQL override for test runs (port 3307) |

## Prerequisites

- Docker and Docker Compose v2
- `curl`, `python3`, `mysql` client

## Usage

### 1. Start the system

```bash
# From train-ticket-aitest/
docker compose up -d --build
```

### 2. Seed the databases

Wait for all services to start (JPA creates schemas on first boot), then:

```bash
mysql -h127.0.0.1 -P3306 -uroot -p'admin@123#' < synthetic-data/output/seed-all.sql
```

### 3. Register test users via API

```bash
GATEWAY=http://localhost:8888 bash synthetic-data/output/setup-auth.sh
```

### 4. Run EvoMaster with seeded Postman collection

```bash
java -jar evomaster.jar \
  --blackBox true \
  --seedTestCases true \
  --seedTestCasesPath synthetic-data/output/postman_seed.json \
  --bbProbabilityUseDataPool 0.9 \
  --outputFolder evomaster-config/generated-tests \
  --maxTime 1h
```

## Service name swap (important)

`ts-preserve-service` hosts `/api/v1/orderservice` (order CRUD).
`ts-order-service` hosts `/api/v1/preserveservice` (booking logic).

## Test credentials

- Username pattern: `wei_zhang`, `fang_li`, … (50 users)
- Password: `password123`
- Admin: `admin` / `222222`

## Visualizing the flow graph

```bash
npx @mermaid-js/mermaid-cli -i output/flow-graph.mmd -o output/flow-graph.png
# or paste into https://mermaid.live
```
