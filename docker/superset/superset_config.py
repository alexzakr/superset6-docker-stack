import os
from celery.schedules import crontab


def env(name: str, default: str) -> str:
    return os.getenv(name, default)


REDIS_HOST = env("REDIS_HOST", "redis")
REDIS_PORT = env("REDIS_PORT", "6379")
REDIS_CELERY_DB = env("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = env("REDIS_RESULTS_DB", "1")

class CeleryConfig:  # noqa: D101
    broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
    result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
    imports = ("superset.sql_lab", "superset.tasks.scheduler")
    task_acks_late = True
    worker_prefetch_multiplier = 10
    task_annotations = {
        "sql_lab.get_sql_results": {"rate_limit": "100/s"},
    }
    beat_schedule = {
        "reports.scheduler": {
            "task": "reports.scheduler",
            "schedule": crontab(minute="*", hour="*"),
        },
        "reports.prune_log": {
            "task": "reports.prune_log",
            "schedule": crontab(minute=10, hour=0),
        },
    }


CELERY_CONFIG = CeleryConfig

RESULTS_BACKEND = {
    "type": "RedisCache",
    "host": REDIS_HOST,
    "port": REDIS_PORT,
    "key_prefix": "superset_results",
    "db": REDIS_RESULTS_DB,
}

FEATURE_FLAGS = {
    "ALERT_REPORTS": True,
}
