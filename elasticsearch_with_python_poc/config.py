import os


class Config:
    def __init__(self):
        self.es_batch_size = None
        self.es_url = None
        self.query_return_length = None

    @classmethod
    def default(cls):
        output = cls()
        output.es_url = "http://localhost:9200/" if os.environ.get("ES_URL") is None else os.environ["ES_URL"]
        output.query_return_length = 10 if os.environ.get("QUERY_RETURN_LENGTH") is None else os.environ[
            "QUERY_RETURN_LENGTH"]

        return output
