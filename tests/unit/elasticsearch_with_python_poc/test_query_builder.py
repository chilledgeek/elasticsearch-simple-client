import json
from unittest import TestCase

from elasticsearch_with_python_poc.query_builder import QueryBuilder


class TestQueryBuilder(TestCase):
    def setUp(self) -> None:
        self.sut = QueryBuilder()

    def test_make_should_append_to_make_query(self):
        # act
        self.sut.must("make whatever")

        # assert
        self.assertIn("make whatever", self.sut._query["query"]["bool"]["must"][0]["match"]["description"]["query"])

    def test_should_should_append_to_should_query(self):
        # act
        self.sut.should("should whatever")

        # assert
        self.assertIn("should whatever",
                      self.sut._query["query"]["bool"]["should"][0]["match"]["description"]["query"])

    def test_should_build_query(self):
        # arrange
        expected_result = json.dumps({"size": 10, "query": {"bool": {"must": [
            {"match": {"description": {"query": "whatever to make", "fuzziness": "AUTO", "prefix_length": 0}}}],
                                                                     "should": [{"match": {
                                                                         "description": {"query": "whatever should",
                                                                                         "fuzziness": "AUTO",
                                                                                         "prefix_length": 0}}}]}}})
        self.sut.should("whatever should")
        self.sut.must("whatever to make")

        # act
        result = self.sut.build()

        # assert
        self.assertEqual(result, expected_result)
