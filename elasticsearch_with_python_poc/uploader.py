import pandas as pd
from elasticsearch import Elasticsearch

from elasticsearch_with_python_poc.config import Config

class Uploader:
    def __init__(self):
        self.config = Config.default()
        self.es = Elasticsearch([self.config.es_url], timeout=60)


    def post_df_as_body_to_elasticsearch(self, annotated_descriptions: pd.DataFrame) -> None:
        post_body = "".join(['{"index":{"_index": "transactions", "_id": "' + str(entry[0].replace(" ","-")) + '"}}\n' +
                               '{"description": "' + str(entry[0]) +
                               '", "annotated category": "' + str(entry[1]) + '"}\n'
                               for entry in annotated_descriptions.values])

        self.es.bulk(post_body)
