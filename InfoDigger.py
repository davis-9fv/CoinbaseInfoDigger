from coinbase.wallet.client import Client
import time
from elasticsearch import Elasticsearch
from datetime import datetime

# GitPython
# python-dateutil
# https://elasticsearch-py.readthedocs.io/en/master/
# https://docs.objectrocket.com/elastic_python_examples.html

INDEX = 'coinbase'
DOC_TYPE = 'rates'

client = Client("zhtXa1PEK0J6tzZ2", "pS9sqBNMAWVLfJWGXk36wLuCb1OMQnIF")
rates = client.get_exchange_rates(currency='BTC')
rates['time'] = time.time()

print(rates)

es = Elasticsearch(
    ['192.168.1.7'],
    scheme="http",
    port=9200
)

res = es.index(index=INDEX, doc_type=DOC_TYPE, body=rates)
print(res)

