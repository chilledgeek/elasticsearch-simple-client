import json

from elasticsearch import Elasticsearch

from elasticsearch_with_python_poc.config import Config


class QueryBuilder:
    def __init__(self):
        self._config = Config.default()
        self._query: dict = {
            "size": self._config.query_return_length,
            "query": {
                "bool": {
                    "must": [],
                    "should": []
                }
            }
        }

    @staticmethod
    def _match(key: str, value: str) -> dict:
        return {
            "match": {
                key: {
                    "query": value,
                    "fuzziness": "AUTO",
                    "prefix_length": 0
                }
            }
        }

    def must(self, value: str, key: str = "description"):
        self._query["query"]["bool"]["must"].append(self._match(key, value))
        return self

    def should(self, value: str, key: str = "description"):
        self._query["query"]["bool"]["should"].append(self._match(key, value))
        return self

    def build(self):
        return json.dumps(self._query)
