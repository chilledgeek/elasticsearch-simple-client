import json
import numpy as np
import pandas as pd


class UploadQueryBuilder:
    """
    Query builder for uploading pandas dataframe to elasticsearch
    Works for flat df only for now
    """

    @staticmethod
    def _build_entry_header(index: str, id_for_entry: None) -> str:
        entry_header = dict(index=dict())

        entry_header["index"]["_index"] = index

        if id_for_entry is not None:
            entry_header["index"]["_id"] = id_for_entry

        return json.dumps(entry_header)

    @staticmethod
    def _build_entry_data(keys, df_row: np.array) -> str:

        entry_data = dict()
        for n, key in enumerate(keys):
            entry_data[key] = str(df_row[n])

        return json.dumps(entry_data)

    def build(self,
              df: pd.DataFrame,
              index: str) -> str:

        keys = df.keys()

        items = [self._build_entry_header(index=index, id_for_entry=entry[0]) + "\n" +
                 self._build_entry_data(keys, entry)
                 for entry in df.values]

        return "\n".join(items)
