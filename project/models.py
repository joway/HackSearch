from django.db import models

# Create your models here.
from jsonfield import JSONField

from project.constants import PROJECT_STATUS_CHOICES, PROCESS_TYPE_CHOICES, ProjectStatus, HTTP_METHOD_CHOICES, \
    VALID_DOMAIN_MODEL_CHOICES, ValidDomainModels, WEBSITE_CATALOG_CHOICES
from utils.constants import HTTPMethod, ProcessType
from utils.helpers import gen_uuid, get_root_domain


class Project(models.Model):
    proj_id = models.CharField('项目id', primary_key=True, max_length=56, unique=True,
                               default=gen_uuid)

    name = models.CharField('项目名', max_length=56, unique=True)

    catalog = models.CharField('目录', choices=WEBSITE_CATALOG_CHOICES, max_length=32)

    status = models.IntegerField(choices=PROJECT_STATUS_CHOICES, default=ProjectStatus.WAIT_FOR_START)
    entry_url = models.URLField('入口链接')
    domain = models.CharField(max_length=255, null=True, blank=True)

    process_type = models.IntegerField('处理类型', choices=PROCESS_TYPE_CHOICES,
                                       default=ProcessType.CSS_SELECT)
    http_method = models.IntegerField('HTTP方法', choices=HTTP_METHOD_CHOICES,
                                      default=HTTPMethod.GET)

    headers = models.TextField('HTTP Headers', null=True)
    cookies = models.TextField('Cookies', null=True)

    valid_domain_model = models.IntegerField('合法域名模式', choices=VALID_DOMAIN_MODEL_CHOICES,
                                             default=ValidDomainModels.FULL_DOMAIN)

    valid_path_regex = models.CharField('合法Path正则', max_length=56, default=r'^', null=True)

    payload = JSONField('参数', default={})
    rules = JSONField('内容提取映射规则', default={})

    created_at = models.DateTimeField('创建于', auto_now_add=True)
    last_fetch = models.DateTimeField('上一次抓取', auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.domain and self.entry_url:
            self.domain = get_root_domain(self.entry_url)
        super().save(*args, **kwargs)
