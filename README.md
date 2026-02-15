# Apache Superset 6 Docker Stack

Production-ready Docker Compose stack for running Apache Superset `6.0.0`.

## Services

- `superset` - Superset web application (`:8088`)
- `superset-init` - initial bootstrap (DB migrations, admin creation, `superset init`)
- `superset-worker` - Celery worker for SQL Lab and background tasks
- `superset-worker-beat` - Celery beat (scheduler/reports)
- `db` - PostgreSQL 16 (metadata database)
- `redis` - broker/result backend/cache
- `flower` - optional Celery monitoring (`:5555`, `observability` profile)

## Repository Structure

- `docker-compose.yml` - main stack definition
- `docker/superset/Dockerfile` - custom image based on `apache/superset:6.0.0`
- `docker/superset/superset_config.py` - Superset/Celery configuration
- `docker/superset/init-superset.sh` - bootstrap initialization script
- `.env.example` - environment variables example

## Quick Start

```bash
cp .env.example .env
# Set secure values before startup:
# SUPERSET_SECRET_KEY, SUPERSET_ADMIN_PASSWORD, POSTGRES_PASSWORD

docker compose build superset-init
docker compose up -d
```

Verification:

```bash
docker compose ps
docker compose logs -f superset-init
```

Superset UI: `http://localhost:8088`

## Optional: Flower

```bash
docker compose --profile observability up -d flower
```

Flower UI: `http://localhost:5555`

## Upgrade Flow

1. Update the base image tag in `docker/superset/Dockerfile`.
2. Rebuild: `docker compose build superset-init`.
3. Restart: `docker compose up -d`.

## Notes

- To avoid image build race conditions, `build` is defined only for `superset-init`; other services use the already built `local/superset:6.0.0` image.
- `depends_on` plus `healthcheck` ensure runtime startup ordering.
