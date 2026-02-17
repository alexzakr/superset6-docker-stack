FROM apache/superset:6.0.0

USER root

COPY requirements.txt /app/requirements.txt
RUN . /app/.venv/bin/activate && \
    uv pip install --no-cache-dir -r /app/requirements.txt && \
    apt-get update && apt-get install -y --no-install-recommends curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY init-superset.sh /app/docker/init/init-superset.sh
RUN chmod +x /app/docker/init/init-superset.sh

USER superset
