from config.celery import app
from spider.fetcher.services import FetcherService
from spider.processor.tasks import process


@app.task(routing_key='fetcher')
def fetch(task):
    process_task = FetcherService.fetch(task=task)
    if process_task:
        process.delay(process_task)
