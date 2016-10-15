from utils.helpers import url_hash, clean_links, init_task_options
from utils.redis_client import redis_client


class SchedulerService(object):
    @classmethod
    def scheduling_tasks(cls, proj_id: str, links: [], options: []):
        tasks = []
        links = clean_links(proj_id, links)

        # 为了部分解决锁问题
        for l in links:
            redis_client.sadd(proj_id, url_hash(l))
        print('爬取链接 %s' % str(links))

        for link in links:
            task = dict({
                'proj_id': proj_id,
                'task_id': url_hash(link),
                'url': link}, **options)
            task = init_task_options(task)
            tasks.append(task)

            cls.scheduling_task(task)
        return tasks

    @classmethod
    def scheduling_task(cls, task):
        from spider.fetcher.tasks import fetch
        fetch.delay(task)
