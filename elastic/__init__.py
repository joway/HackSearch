from elasticsearch import Elasticsearch

from config.settings import ELASTIC_HOSTS, ELASTIC_AUTH_USER, ELASTIC_AUTH_PASSWORD

elatic = Elasticsearch(
    ELASTIC_HOSTS,
    # http_auth=(ELASTIC_AUTH_USER, ELASTIC_AUTH_PASSWORD),
)
