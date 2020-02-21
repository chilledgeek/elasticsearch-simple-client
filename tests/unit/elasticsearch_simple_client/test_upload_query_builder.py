import json
from unittest import TestCase
from unittest.mock import Mock

import pandas as pd

from elasticsearch_simple_client.config import Config
from elasticsearch_simple_client.upload_query_builder import UploadQueryBuilder
from tests.common.fixtures import Fixtures


class TestUploadQueryBuilder(TestCase):
    def setUp(self) -> None:
        self.sut = UploadQueryBuilder()
        self.fixture = pd.DataFrame(
            {"column1": ["column1value1", "column1value2"],
             "column2": ["column2value1", "column2value2"],
             "column3": ["column3value1", "column3value2"]}
        )

    def test_build_calls_build_entry_header_expected_number_of_times(self):
        # arrange
        self.sut._build_entry_header = Mock(return_value="build_entry_header")

        # act
        self.sut.build(df=self.fixture,
                       index="some index")

        # assert
        self.assertEqual(self.sut._build_entry_header.call_count, 2)

    def test_build_calls_build_entry_data_expected_number_of_times(self):
        # arrange
        self.sut._build_entry_data = Mock(return_value="build_entry_data")

        # act
        self.sut.build(df=self.fixture,
                       index="some index")

        # assert
        self.assertEqual(self.sut._build_entry_data.call_count, 2)

    def test_build_should_return_as_expected(self):
        # arrange
        expected_result = Fixtures.get_upload_query()

        # act
        result = self.sut.build(df=self.fixture,
                                index=Config.default().es_index)

        # assert
        self.assertEqual(result, expected_result)
