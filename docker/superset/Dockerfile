FROM apache/superset:6.0.0

USER root

RUN /app/.venv/bin/pip install --no-cache-dir psycopg2-binary redis && \
    apt-get update && apt-get install -y --no-install-recommends curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY init-superset.sh /app/docker/init/init-superset.sh
RUN chmod +x /app/docker/init/init-superset.sh

USER superset
