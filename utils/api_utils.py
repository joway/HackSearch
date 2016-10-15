import requests

from config.settings import SCHEDULER_CALLBACK_API
from utils.exceptions import CallbackException


def callback(proj_id, inter_links, retry=True):
    try:
        req = requests.post(url=SCHEDULER_CALLBACK_API, data={
            'proj_id': proj_id,
            'inter_links': inter_links
        })
        return req.json()
    except Exception:
        if retry:
            return callback(proj_id, inter_links, False)
        else:
            # TODO: 报告回调错误
            raise CallbackException
