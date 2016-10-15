import requests

from utils.constants import ProcessType


class APIService(object):
    BASE_API = 'http://hack.joway.wang:8000/'

    @classmethod
    def create_article(cls, url, title, content, keyset):
        api = cls.BASE_API + 'article/'
        data = {
            'url': url,
            'title': title,
            'content': content,
            'keyset': " ".join(keyset)
        }
        resp = requests.post(url=api, data=data)
        return resp

    @classmethod
    def create_proj(cls, name, entry_url):
        api = cls.BASE_API + 'proj/'
        data = {
            'name': name,
            'entry_url': entry_url,
            'catalog': 'tech',
            'process_type': ProcessType.AUTO_MATCH
        }
        resp = requests.post(url=api, data=data)
        return resp
