import json
from config import *
from elasticsearch import Elasticsearch
import elasticsearch


my_instance = Elasticsearch(es_host,http_auth=(es_user, es_password),use_ssl=True,verify_certs=False)

if not my_instance:
    print("Connection Error")
else:
    print("connection successful")

def search_es(es_query,search_index="app_wallet_01"):
    response = my_instance.search(index=search_index, body=es_query)
    return response


es_query = {
  "size": 1000,
  "query": {
    "match_all": {}
  }
}

if __name__ == "__main__":
    es_result = search_es(es_query)
    print(json.dumps(es_result.get("hits","").get("hits"), indent=2))
else:
    print("connect module imported")

# es_result = search_es(es_query,search_index="kibana_sample_data_ecommerce")
# print(f"found {len(es_result.get('hits','').get('hits'))} documents in given query for commerce index")