""" 抓取器
从抓取urls
"""
import requests

from utils.constants import HTTPMethod
from utils.helpers import is_duplicates_link


class FetcherService(object):
    @classmethod
    def packing_task(cls, task, request):
        task['content'] = request.text
        task['encoding'] = request.encoding
        task['status_code'] = request.status_code
        return task

    @classmethod
    def init_task(cls, task):
        task['headers'] = task['headers'] if task['headers'] else {'Connection': 'close'}

    @classmethod
    def fetch(cls, task):
        if task['http_method'] == HTTPMethod.GET:
            return cls.fetch_get(task)
        elif task['http_method'] == HTTPMethod.POST:
            return cls.fetch_post(task)

    @classmethod
    def fetch_get(cls, task):
        req = requests.get(task['url'], params=task['payload'], headers=task['headers'])
        return cls.packing_task(task, req)

    @classmethod
    def fetch_post(cls, task):
        req = requests.post(task['url'], data=task['payload'], headers=task['headers'])
        return cls.packing_task(task, req)
