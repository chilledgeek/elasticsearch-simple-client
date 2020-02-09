# Elasticsearch with Python Proof of Concept (PoC)
## Background
- This repo has some code and notes on exploring the use of elasticsearch with python
- Sample dataset is a set of transactions with roughly annotated categories
- Index is the description (spaces substituted with hyphens), each entry with a description and category field
- One of the aims is to load such transactions to elasticsearch and use the fuzzy matching to see how well it does 
in predicting new transactions
- This will be compared to a supervised machine learning approach

## Setting up
- To start elasticsearch docker:
  - `sudo docker pull elasticsearch:7.5.2`
  - `docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.5.2`

## Loading data using python (from a dataframe)
```
import pandas as pd

from elasticsearch_with_python_poc.uploader import Uploader

uploader = Uploader()
df = pd.read_csv("tests/common/annotated_descriptions.csv"))

uploader.post_df_as_body_to_elasticsearch(df)
```

## Searching data
### Python
```
import pandas as pd

from elasticsearch_with_python_poc.searcher import Searcher

searcher = Searcher()

searcher.execute_search(musts=["exact match with some fuzziness"], 
                        shoulds=["less exact matches allowed"])
```
### Via a web get (e.g. using postman)
- Send a GET to 'https:localhost:9200/_search'
- ``` json
  {
      "from": 0,
      "size": 20,
      "query": {
          "bool": {
              "must": [
                  {
                      "match": {
                          "description": {
                              "query": "AMAZON",
                              "fuzziness": "AUTO",
                              "prefix_length": 0
                          }
                      }
                  }
              ],
              "should": [
                  {
                      "match": {
                          "description": {
                              "query": "MARKETPLACE",
                              "fuzziness": "AUTO",
                              "prefix_length": 0
                          }
                      }
                  }
              ]
          }
      }
  }
  ```

## Future work
- Set up for multiple tag (not all transactions should have just one category? 
e.g. transactions at a petrol station can count as petrol, but sometimes one can buy snacks/food as well there)