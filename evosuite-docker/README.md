# EvoSuite Docker Setup for Train-Ticket

This directory contains Docker-based tools for running EvoSuite automated test generation on the Train-Ticket microservices.

## Prerequisites

- Docker installed and running
- Docker Compose v2.0+

## Quick Start

### 1. Generate tests for a specific class

```bash
# Generate tests for a utility class (recommended starting point)
./run-evosuite.sh ts-admin-service \
    com.cloudhubs.trainticket.adminservice.util.StringUtils

# Generate tests for an entity class
./run-evosuite.sh ts-admin-service \
    com.cloudhubs.trainticket.adminservice.entity.Contacts
```

### 2. Generate tests for all classes in a service

```bash
./run-evosuite.sh ts-admin-service
```

### 3. Generate tests for all microservices

```bash
./run-all-services.sh
```

## Configuration

Set environment variables to customize behavior:

| Variable | Default | Description |
|----------|---------|-------------|
| `SEARCH_BUDGET` | 120 | Time in seconds per class |
| `CORES` | 4 | Number of CPU cores to use |
| `CRITERION` | LINE:BRANCH:EXCEPTION:WEAKMUTATION:OUTPUT:METHOD | Coverage criteria |

Example:
```bash
SEARCH_BUDGET=300 CORES=8 ./run-evosuite.sh ts-admin-service
```

## Output

Generated tests are placed in each service directory:

```
ts-admin-service/
├── evosuite-tests/           # Generated JUnit tests
│   └── com/cloudhubs/.../
│       ├── *_ESTest.java              # Test cases
│       └── *_ESTest_scaffolding.java  # Test infrastructure
└── evosuite-report/          # Coverage statistics
    └── statistics.csv
```

## Building the Docker Image Manually

```bash
docker build -t evosuite-trainticket:1.2.0 .
```

## Running EvoSuite Directly

```bash
# Show help
docker run --rm evosuite-trainticket:1.2.0 -help

# List all parameters
docker run --rm evosuite-trainticket:1.2.0 -listParameters
```

## Troubleshooting

### Compilation Errors

If you see Java version errors during compilation, ensure you're using the Java 11 Maven image:
```bash
docker run --rm -v "$(pwd):/project" -w /project \
    maven:3.8.6-eclipse-temurin-11 \
    mvn clean compile -DskipTests \
    -Dmaven.compiler.source=11 \
    -Dmaven.compiler.target=11
```

### Out of Memory

Increase Docker memory allocation or reduce CORES:
```bash
CORES=2 ./run-evosuite.sh ts-admin-service
```

### Slow Generation

For faster results with lower coverage:
```bash
SEARCH_BUDGET=30 ./run-evosuite.sh ts-admin-service
```

## How It Works

The script performs Java 17 to Java 11 cross-compilation:

1. **Source Conversion**: Copies source files and converts `jakarta.*` imports to `javax.*`
2. **Cross-Compilation**: Uses Spring Boot 2.7.x (Java 11 compatible) instead of 3.x
3. **Dependency Collection**: Copies all Maven dependencies to a single directory
4. **EvoSuite Generation**: Runs EvoSuite with `-generateMOSuite` for multi-objective test generation

### Limitations

- **Spring Controllers**: Controllers with complex Spring dependencies may require manual review
- **Config Classes**: Security configuration classes are excluded from compilation
- **Coverage**: Typical coverage ranges from 70-90% depending on class complexity

## EvoSuite Version

This setup uses EvoSuite v1.2.0, which supports:
- Java 8-11 (Java 11 via cross-compilation from Java 17)
- JUnit 4 output with EvoSuite runtime
- DynaMOSA algorithm (multi-objective search)

## References

- [EvoSuite Website](https://www.evosuite.org/)
- [EvoSuite GitHub](https://github.com/EvoSuite/evosuite)
- [EvoSuite Documentation](https://www.evosuite.org/documentation/)
