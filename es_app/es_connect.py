import json
from config import *
from elasticsearch import Elasticsearch

my_instance = Elasticsearch(es_host,http_auth=(es_user, es_password),use_ssl=True,verify_certs=False)

if not my_instance:
    print("Connection Error")