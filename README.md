# Elasticsearch simple client
| Code quality checks  | Status |
| ------------- |:-------------:|
| CodeFactor      |  [![Codefactor](https://www.codefactor.io/repository/github/chilledgeek/elasticsearch-simple-client/badge?style=plastic)](https://www.codefactor.io/repository/github/chilledgeek/elasticsearch-simple-client) |
| CircleCI |  [![CircleCI](https://circleci.com/gh/chilledgeek/elasticsearch-simple-client.svg?style=svg)](https://circleci.com/gh/chilledgeek/elasticsearch-simple-client)|
| Codecov | [![codecov](https://codecov.io/gh/chilledgeek/elasticsearch-simple-client/branch/master/graph/badge.svg)](https://codecov.io/gh/chilledgeek/elasticsearch-simple-client)|

## Background
- This repo is a package that interfaces with [elasticsearch](https://www.elastic.co/) that allows simple data uploading and querying with python
- Below are some basic instructions on how to use the code.
- A sample use case for this code is also illustrated at the end of this readme

## How to use
### Starting the elasticsearch docker run
- `sudo docker pull elasticsearch:7.5.2`
- `docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.5.2`

### Loading from a csv
```
import pandas as pd
from elasticsearch_simple_client.uploader import Uploader

uploader = Uploader()
df = pd.read_csv("example/descriptions_with_categories.csv"))

uploader.post_df(df)
```

### Searching data
```
import pandas as pd

from elasticsearch_with_python_poc.searcher import Searcher

searcher = Searcher()

result = searcher.execute_search(musts=["exact match with some fuzziness"], 
                                 shoulds=["less exact matches allowed"])
```

### Deleting data (not implemented by this python repo)
- To [clear an elasticsearch index](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-delete-index.html)
just run this in command line:
  - `curl -X DELETE "localhost:9200/<index_name>"`

## Sample Application (categorising new short text descriptions)
- An [example notebook](example/Categorisation%20of%20short%20text%20descriptions.ipynb) is included in this repo to demonstrate
how this code can be used.
- The use case in this example is to categorise account transactions based on description
(e.g. the description "ANSTRUTHER FISH BAR AND ANSTRUTHER GBR" should be categorised as "EAT OUT")
- Some anonymised data used in the notebook can be found [in the example folder](example/descriptions_with_categories.csv)
- Once transactions (with known descriptions) are added to [elasticsearch](https://www.elastic.co/), the simple fuzzy string lookup function of 
 [elasticsearch](https://www.elastic.co/) can be applied to predict new transactions simply by looking up the transaction (of known category) 
 that best matches the new one
- While machine learning models can also be trained using transactions with known descriptions,
this example demonstrates that fuzzy string matching on its own can sometimes be a simpler yet elegant solution

![elasticsearch_and_ml_performance](https://user-images.githubusercontent.com/44337585/75066979-ef75b700-54e3-11ea-8249-8e1d9fa31bdf.png)
