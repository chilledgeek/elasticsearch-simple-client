from unittest import TestCase

import os
from unittest.mock import Mock

import pandas as pd

from elasticsearch_with_python_poc.uploader import Uploader


class TestUploader(TestCase):
    def setUp(self) -> None:
        self.sut = Uploader()
        self.fixture = pd.read_csv(os.path.join(os.path.dirname(__file__), "../../common/annotated_descriptions.csv"))

    def test_init_returns_non_none_config(self):
        # assert
        self.assertIsNotNone(self.sut.config)

    def test_init_returns_non_none_es(self):
        # assert
        self.assertIsNotNone(self.sut.es)

    def test_post_df_as_body_to_elasticsearch_calls_es_bulk_once(self):
        # arrange
        self.sut.es.bulk = Mock()

        # act
        self.sut.post_df_as_body_to_elasticsearch(self.fixture)

        # assert
        self.sut.es.bulk.assert_called_once()
