import json

import pandas as pd

from elasticsearch_simple_client.config import Config


class Fixtures:
    @staticmethod
    def get_df_fixture():
        fixture = pd.DataFrame(
            {"column1": ["column1value1", "column1value2"],
             "column2": ["column2value1", "column2value2"],
             "column3": ["column3value1", "column3value2"]}
        )

        return fixture

    @staticmethod
    def get_upload_query():
        return "\n".join(
            [
                '{"index": {"_index": "simple_text", "_id": "column1value1"}}',
                '{"column1": "column1value1", "column2": "column2value1", "column3": "column3value1"}',
                '{"index": {"_index": "simple_text", "_id": "column1value2"}}',
                '{"column1": "column1value2", "column2": "column2value2", "column3": "column3value2"}'
            ]
        )

    @staticmethod
    def get_search_query():
        return json.dumps(
            {"size": Config.default().query_return_length,
             "query": {
                 "bool": {
                     "must": [
                         {
                             "match": {
                                 "description": {
                                     "query": "whatever must", "fuzziness": "AUTO", "prefix_length": 0
                                 }
                             }
                         }
                     ],
                     "should": [
                         {
                             "match": {
                                 "description": {
                                     "query": "whatever should",
                                     "fuzziness": "AUTO",
                                     "prefix_length": 0
                                 }
                             }
                         }
                     ]
                 }
             }
             }
        )
