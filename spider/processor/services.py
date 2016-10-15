import json

from bs4 import BeautifulSoup
from lxml import etree
from lxml.etree import LxmlSyntaxError

from spider.processor.extractor import Extractor
from utils.constants import ProcessType
from utils.helpers import extract_valid_links, normalize

MIN_CONTENT_LINE = 10


class ProcessorService(object):
    @classmethod
    def process(cls, task):
        process_type = task['process_type']
        if process_type == ProcessType.XPATH:
            mapping = cls.process_xpath(task['content'], task['rules'])
        elif process_type == ProcessType.CSS_SELECT:
            mapping = cls.process_css_select(task['content'], task['rules'])
        elif process_type == ProcessType.JSON:
            mapping = cls.process_json(task['content'], task['rules'])
        elif process_type == ProcessType.AUTO_MATCH:
            mapping = cls.process_auto_match(task['content'], task['rules'])
            mapping['content'] = normalize(task['content'])
        else:
            raise Exception

        # 通知 scheduler 进行后续链接爬取
        valid_links = extract_valid_links(task['content'], task['valid_link_regex'], task['domain'])
        result = cls.prepare_result(task['proj_id'], task['url'], task['catalog'], task['domain'], task['task_id'],
                                    mapping,
                                    valid_links)
        return result

    @classmethod
    def process_auto_match(cls, content, rules=None):
        return cls.process_css_select(content, rules={
            'title': 'title',
        })

    @classmethod
    def process_css_select(cls, content, rules):
        try:
            soup = BeautifulSoup(content, 'lxml')
        except LxmlSyntaxError:
            #     log
            return {}
        mapping = {}
        for rule in rules:
            try:
                mapping[rule] = soup.select(rules[rule])[0].get_text()
            except ValueError:
                mapping[rule] = 'Unsupported or invalid CSS selector: "%s"' % rule
            except IndexError:
                # 未找到内容
                pass
        return mapping

    @classmethod
    def process_xpath(cls, content, rules):
        html = etree.HTML(content)
        mapping = {}
        for rule in rules:
            mapping[rule] = html.xpath(rules[rule])
        return mapping

    @classmethod
    def process_json(cls, content, rules):
        mapping = {}
        json_obj = json.loads(content)
        # TODO : json 选择器
        for rule in rules:
            mapping[rule] = json_obj[rule]
        return mapping

    @classmethod
    def prepare_result(cls, proj_id, url, catalog, domain, task_id, mapping, valid_links=[]):
        mapping['url'] = url
        return {
            'proj_id': proj_id,
            'url': url,
            'catalog': catalog,
            'domain': domain,
            'task_id': task_id,
            'mapping': mapping,
            'valid_links': valid_links,
        }
