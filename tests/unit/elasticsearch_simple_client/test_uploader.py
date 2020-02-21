from unittest import TestCase
from unittest.mock import Mock, patch

import pandas as pd

from elasticsearch_simple_client.uploader import Uploader


class TestUploader(TestCase):
    def setUp(self) -> None:
        self.sut = Uploader()
        self.sut._es.bulk = Mock()

    @patch("elasticsearch.Elasticsearch.__init__", return_value=None)
    def test_search_loads_es_url_not_from_config_when_es_url_specified(self, mock_es_init):
        # act
        Uploader(es_url="whatever")

        # assert
        mock_es_init.assert_called_once_with(["whatever"], timeout=60)

    def test_init_returns_non_none_config(self):
        # assert
        self.assertIsNotNone(self.sut._config)

    def test_init_returns_non_none_es(self):
        # assert
        self.assertIsNotNone(self.sut._es)

    def test_init_returns_non_none_query_builder(self):
        # assert
        self.assertIsNotNone(self.sut._query_builder)

    def test_post_df_calls_es_bulk_once(self):
        # act
        self.sut.post_df(pd.DataFrame())

        # assert
        self.sut._es.bulk.assert_called_once()

    def test_post_df_with_index_is_passed_to_query_builder(self):
        # arrange
        self.sut._query_builder.build = Mock()
        mock_df = Mock()

        # act
        self.sut.post_df(df=mock_df,
                         index="some index")

        # assert
        self.sut._query_builder.build.assert_called_once_with(df=mock_df,
                                                              index="some index")
