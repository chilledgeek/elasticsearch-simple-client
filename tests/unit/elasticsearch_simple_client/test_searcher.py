from unittest import TestCase
from unittest.mock import Mock, patch
from elasticsearch_simple_client.searcher import Searcher


class TestSearcher(TestCase):
    def setUp(self) -> None:
        self.sut = Searcher()

    @patch("elasticsearch.Elasticsearch.search")
    def test_execute_search_calls_build_single_index_search_query(self, mock_es_search):
        # arrange
        self.sut._builder.build_single_index_search_query = Mock()

        # act
        self.sut.execute_search(musts=["123"], shoulds=["should only"], field="description")

        # assert
        self.sut._builder.build_single_index_search_query.assert_called_once_with(
            musts=["123"], shoulds=["should only"], field="description",
            query_return_length=1)

    @patch("elasticsearch.Elasticsearch.search")
    def test_execute_search(self, mock_es_search):
        # arrange
        query = self.sut._builder.build_single_index_search_query(musts=["123"],
                                                                  shoulds=["should only"],
                                                                  field="description",
                                                                  query_return_length=1)

        # act
        self.sut.execute_search(musts=["123"], shoulds=["should only"], field="description", )

        # assert
        mock_es_search.assert_called_once_with(body=query, index="simple_text")

    @patch("elasticsearch.Elasticsearch.__init__", return_value=None)
    def test_search_loads_es_url_not_from_config_when_es_url_specified(self, mock_es_init):
        # act
        Searcher(es_url="whatever")

        # assert
        mock_es_init.assert_called_once_with(["whatever"], timeout=60)
