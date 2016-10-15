from kombu import Queue

from config.settings import REDIS_CONN_URL

BROKER_URL = REDIS_CONN_URL + '/0'
CELERY_RESULT_BACKEND = REDIS_CONN_URL + '/1'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True

CELERY_TASK_RESULT_EXPIRES = 120  # celery任务执行结果的超时时间
CELERYD_CONCURRENCY = 50  # celery worker的并发数 也是命令行-c指定的数目
CELERYD_PREFETCH_MULTIPLIER = 4  # celery worker 每次去取任务的数量
CELERYD_MAX_TASKS_PER_CHILD = 100  # 每个worker执行了多少任务就会死掉, 防止内存泄漏
CELERYD_TASK_TIME_LIMIT = 60  # 单个任务执行限制时间

CELERY_IMPORTS = (
    "spider.scheduler.tasks",
    "spider.fetcher.tasks",
    "spider.processor.tasks",
    "spider.pipeline.tasks",
)

CELERY_QUEUES = (
    Queue('scheduler', routing_key='scheduler'),
    Queue('fetcher', routing_key='fetcher'),
    Queue('processor', routing_key='processor'),
    Queue('pipeline', routing_key='pipeline'),
)
