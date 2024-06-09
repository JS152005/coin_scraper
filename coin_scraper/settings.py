INSTALLED_APPS = [
   ...
    'est_framework',
    'api',
    'django_celery_results',  # For storing Celery results
    'django_celery_beat',  # For scheduling tasks
]

# Celery Configuration
CELERY_BROKER_URL = 'edis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Celery Beat Configuration
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'

# Redis Configuration
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

# Add celery to the Django apps
INSTALLED_APPS += ('django_celery_results', 'django_celery_beat')

# Celery Task Settings
CELERY_TASK_DEFAULT_QUEUE = 'default'
CELERY_TASK_DEFAULT_EXCHANGE = 'default'
CELERY_TASK_DEFAULT_ROUTING_KEY = 'default'

# Celery Worker Settings
CELERY_WORKER_CONCURRENCY = 4
CELERY_WORKER_PREFETCH_MULTIPLIER = 4
CELERY_WORKER_MAX_TASKS_PER_CHILD = 200

# Celery Beat Settings
CELERY_BEAT_MAX_LOOP_INTERVAL = 5
CELERY_BEAT_SYNC_EVERY = 1

# Celery Monitoring Settings
CELERY_MONITOR_MAX_TASKS_PER_CHILD = 200
CELERY_MONITOR_MAX_MEMORY_PER_CHILD = 500

# Celery Flower Settings
CELERY_FLOWER_PORT = 5555
CELERY_FLOWER_BASIC_AUTH = 'username:password'