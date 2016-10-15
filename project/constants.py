from utils.constants import ProcessType, HTTPMethod


class ProjectStatus(object):
    WAIT_FOR_START = 1
    RUNNING = 2
    FINISHED = 3
    FAILED = 4


class WebsiteCatalog(object):
    TECH = 'tech'
    BLOG = 'blog'
    TRAVEL = 'travel'
    LITERATURE = 'literature'
    HEALTH = 'health'


WEBSITE_CATALOG_CHOICES = (
    (WebsiteCatalog.TECH, '技术'),
    (WebsiteCatalog.BLOG, '博客'),
    (WebsiteCatalog.TRAVEL, '旅行'),
    (WebsiteCatalog.LITERATURE, '文学'),
    (WebsiteCatalog.HEALTH, '医疗健康'),
)


class ValidDomainModels(object):
    FULL_DOMAIN = 1
    EXTENSIVE = 2
    ALL = 3


PROCESS_TYPE_CHOICES = (
    (ProcessType.CSS_SELECT, 'CSS选择器'),
    (ProcessType.XPATH, 'CSS'),
    (ProcessType.JSON, 'JSON'),
    (ProcessType.AUTO_MATCH, 'AUTO_MATCH'),
)

HTTP_METHOD_CHOICES = (
    (HTTPMethod.GET, 'GET'),
    (HTTPMethod.POST, 'POST'),
)

PROJECT_STATUS_CHOICES = (
    (ProjectStatus.WAIT_FOR_START, '等待开始'),
    (ProjectStatus.RUNNING, '正在运行'),
    (ProjectStatus.FINISHED, '结束'),
    (ProjectStatus.FAILED, '失败'),
)

VALID_DOMAIN_MODEL_CHOICES = (
    (ValidDomainModels.FULL_DOMAIN, '当前Hostname匹配'),
    (ValidDomainModels.EXTENSIVE, '泛域名匹配'),
    (ValidDomainModels.ALL, '通配'),
)
