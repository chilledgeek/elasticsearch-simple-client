import pandas as pd
from elasticsearch import Elasticsearch

from elasticsearch_simple_client.config import Config
from elasticsearch_simple_client.upload_query_builder import UploadQueryBuilder


class Uploader:
    def __init__(self, es_url: str = None):
        self._config = Config.default()
        es_url = self._config.es_url if es_url is None else es_url
        self._es = Elasticsearch([es_url], timeout=60)
        self._query_builder = UploadQueryBuilder()

    def post_df(self,
                df: pd.DataFrame,
                index=None) -> None:
        if index is None:
            index = self._config.es_index

        post_body = self._query_builder.build(df=df,
                                              index=index)

        self._es.bulk(post_body)
