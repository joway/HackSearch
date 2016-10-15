import redis

from config.settings import REDIS_URL_DB, REDIS_PORT, REDIS_HOST, REDIS_PASSWORD

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_URL_DB, password=REDIS_PASSWORD)
