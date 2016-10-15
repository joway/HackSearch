from elastic.services import ElasticService
from hackathon.api import APIService
from hackathon.keyset import get_keyset


class PipelineService(object):
    @classmethod
    def pipeline(cls, result):
        # 存储到 elastic search
        ElasticService.index_doc(
            index=result['catalog'], doc_type=result['domain'],
            doc=result['mapping'], doc_id=result['task_id'])

        # for hackathon
        APIService.create_article(url=result['url'],
                                  title=result['mapping']['title'],
                                  content=result['mapping']['content'],
                                  keyset=get_keyset(result['mapping']['content']))

        return result
