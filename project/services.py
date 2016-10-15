import json

from project.constants import ValidDomainModels
from utils.helpers import get_full_domain, get_root_domain


class ProjectService(object):
    @classmethod
    def gen_project_options(cls, project):
        try:
            rules = json.loads(project.rules) if isinstance(project.rules, str) else project.rules
        except:
            raise Exception('Illegal Rules')
        options = {
            'catalog': project.catalog,
            'domain': project.domain,
            'rules': rules,
            'payload': project.payload,
            'process_type': project.process_type,
            'http_method': project.http_method,
            'headers': project.headers,
            'cookies': project.cookies
        }
        valid_domain_regex = r'^http(s)?://'

        if project.valid_domain_model == ValidDomainModels.FULL_DOMAIN:
            valid_domain_regex += r'%s' % get_full_domain(project.entry_url)
        elif project.valid_domain_model == ValidDomainModels.EXTENSIVE:
            valid_domain_regex += r'([a-z0-9]+[.])%s' % get_root_domain(project.entry_url)
        elif project.valid_domain_model == ValidDomainModels.ALL:
            pass
        options['valid_domain_regex'] = valid_domain_regex
        return options
