import json

class SearchQueryBuilder:
    """
    Query builder to search for single index in elasticsearch with multiple musts or shoulds
    """

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

    def build_single_index_search_query(self,
                                        field: str,
                                        query_return_length: int,
                                        musts: list = None,
                                        shoulds: list = None
                                        ):
        if musts is None:
            musts = []
        if shoulds is None:
            shoulds = []

        query: dict = {
            "size": query_return_length,
            "query": {
                "bool": {
                    "must": [self._match(field, must) for must in musts],
                    "should": [self._match(field, should) for should in shoulds],
                }
            }
        }

        return json.dumps(query)
