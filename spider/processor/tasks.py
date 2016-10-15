import threading

from config.celery import app
from spider.pipeline.tasks import pipeline
from spider.processor.services import ProcessorService
from spider.scheduler.tasks import scheduling
from utils.api_utils import callback
from utils.helpers import extract_options_from_task


@app.task(routing_key='processor')
def process(task):
    result = ProcessorService.process(task)

    if not result:
        print('内容过短')
        return

    # 存储任务
    if result['mapping']:
        resp = pipeline.delay(result)
        resp.wait()

    if task['is_callback']:
        # callback to server
        t = threading.Thread(target=callback, args=(task['proj_id'], result['valid_links']))
        t.start()
    elif result['valid_links']:
        # 直接分发任务
        scheduling.delay(result['proj_id'], result['valid_links'], extract_options_from_task(task))
