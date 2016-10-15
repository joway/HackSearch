from config.celery import app
from spider.pipeline.services import PipelineService


@app.task(routing_key='pipeline')
def pipeline(result):
    print('Saved ' + result['url'])
    PipelineService.pipeline(result)
