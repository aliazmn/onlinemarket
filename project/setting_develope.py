








CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        'LOCATION': 'redis://127.0.0.1:6379',
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient",},
        
    }
}







REDIS_HOST = 'redis://127.0.0.1:6379',
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:6379"
CELERY_TIMEZONE = "Asia/Tehran"
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:6379/1'
CELERY_TASK_SERIALIZER = 'json'
CELERY_CACHE_BACKEND = 'default'
CELERY_RESULT_SERIALIZER = 'json'

