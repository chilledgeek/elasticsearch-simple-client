from elasticsearch import Elasticsearch

from elasticsearch_with_python_poc.config import Config
from elasticsearch_with_python_poc.query_builder import QueryBuilder


class Searcher:
    def __init__(self):
        self.config = Config.default()
        self._es = Elasticsearch([self.config.es_url], timeout=60)
        self._builder = QueryBuilder()

    def _build_query(self, musts: list = None, shoulds: list = None):
        if musts is None:
            musts = []
        if shoulds is None:
            shoulds = []

        [self._builder.must(must) for must in musts]
        [self._builder.should(should) for should in shoulds]

        return self._builder.build()

    def execute_search(self, musts: list = None, shoulds: list = None, index="transactions"):
        query = self._build_query(musts, shoulds)
        es_result = self._es.search(body=query, index=index)
        return es_result