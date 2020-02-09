from unittest import TestCase
from unittest.mock import Mock
from elasticsearch_with_python_poc.searcher import Searcher


class TestSearcher(TestCase):
    def setUp(self) -> None:
        self.sut = Searcher()
        self.sut._es = Mock()
        self.sut._es.search = Mock()

    def test_execute_search_calls_build_query(self):
        # arrange
        self.sut._build_query = Mock()

        # act
        self.sut.execute_search(musts=["123"], shoulds=["should only"])

        # assert
        self.sut._build_query.assert_called_once_with(["123"], ["should only"])

    def execute_search(self):
        # arrange
        query = self.sut._build_query(musts=["123"], shoulds=["should only"])

        # act
        self.sut.execute_search(musts=["123"], shoulds=["should only"])

        # assert
        self.sut._es.search.assert_called_once_with(query, "transactions")
