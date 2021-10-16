import os

MICROSERVICE_NAME = 'get-response-of-container-deployment'

REDIS_HOST = os.environ.get('REDIS_HOST', 'redis-cluster')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)
REDIS_DB = os.environ.get('REDIS_DB', 1)
