PG_DSN = 'postgresql://postgres:postgres@localhost:5432/celery_hw'

EMAIL_SENDER = 'AdvertsAPI <adverts_info@testapi.com>'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/2'

# docker run -d -p 25:25 ixdotai/smtp
# celery -A tasks worker --loglevel=DEBUG -P gevent -E

