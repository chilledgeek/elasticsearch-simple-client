from elasticsearch import Elasticsearch

from elasticsearch_simple_client.config import Config
from elasticsearch_simple_client.search_query_builder import SearchQueryBuilder


class Searcher:
    def __init__(self, es_url: str = None):
        self._config = Config.default()
        self._builder = SearchQueryBuilder()

        es_url = self._config.es_url if es_url is None else es_url

        self._es_connecter = Elasticsearch([es_url], timeout=60)

    def execute_search(self, field: str,
                       musts: list = None,
                       shoulds: list = None,
                       query_return_length=None,
                       index=None):
        if index is None:
            index = self._config.es_index
        if query_return_length is None:
            query_return_length = self._config.query_return_length

        query = self._builder.build_single_index_search_query(musts=musts,
                                                              shoulds=shoulds,
                                                              field=field,
                                                              query_return_length=query_return_length)

        es_result = self._es_connecter.search(body=query, index=index)
        return es_result
