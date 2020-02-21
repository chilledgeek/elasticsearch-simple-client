from unittest import TestCase
from unittest.mock import Mock

from elasticsearch_simple_client.config import Config
from elasticsearch_simple_client.search_query_builder import SearchQueryBuilder
from tests.common.fixtures import Fixtures


class TestSearchQueryBuilder(TestCase):
    def setUp(self) -> None:
        self.sut = SearchQueryBuilder()

    def test_build_single_field_query_should_call_match_expected_number_of_times(self):
        # arrange
        self.sut._match = Mock(return_value="random")

        # act
        self.sut.build_single_index_search_query(
            field="description",
            musts=["whatever must1", "whatever must2"],
            shoulds=["whatever should1", "whatever should2", "whatever should3"],
            query_return_length=1)

        # assert
        self.assertEqual(self.sut._match.call_count, 5)

    def test_build_single_field_query_should_return_as_expected(self):
        # arrange
        expected_result = Fixtures.get_search_query()

        # act
        result = self.sut.build_single_index_search_query(
            field="description",
            musts=["whatever must"],
            shoulds=["whatever should"],
            query_return_length=Config.default().query_return_length)

        # assert
        self.assertEqual(result, expected_result)
