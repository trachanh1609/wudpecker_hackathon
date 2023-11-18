#!/usr/bin/env python3

from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

ES_USERNAME = os.getenv("ES_USERNAME")
ES_PASSWORD = os.getenv("ES_PASSWORD")
INDEX_NAME = os.getenv("INDEX_NAME")


es = Elasticsearch(
    [{'host': 'localhost', 'port': 9200, 'scheme': 'https'}],
    http_auth=(ES_USERNAME, ES_PASSWORD),
    verify_certs=False,
    ca_certs=None,
)

def save_to_es(data):
    es.index(index=INDEX_NAME, body=data)

