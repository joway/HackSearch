from django.conf import settings

from . import elatic


class ElasticService(object):
    @classmethod
    def search(cls, query, index, doc_type=None, paging_size=10, paging_from=0):
        return elatic.search(index=index, doc_type=doc_type, body={"query": {"match": {'title': query}}},
                             params={'size': paging_size, 'from': paging_from})

    @classmethod
    def index_doc(cls, index, doc_type, doc, doc_id=None):
        # log
        return elatic.index(index=index, doc_type=doc_type, body=doc, id=doc_id)

    @classmethod
    def delete(cls, index, doc_type, doc_id):
        return elatic.delete(index=index, doc_type=doc_type, id=doc_id)
