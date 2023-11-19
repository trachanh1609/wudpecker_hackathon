#!/usr/bin/env python3

from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

from models.search_models import SearchItem

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


def search_from_es(data: SearchItem):
    body = {
        "from": 0,
        "size": 10,
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "transcript": data.search_query
                        }
                    }
                ],
                "filter": {
                    "bool": {
                        "must": [
                            {
                                "terms": {
                                    "file_name.enum": data.file_names
                                }
                            }
                        ]
                    }
                }
            },
        }
    }
    res = es.search(index=INDEX_NAME, body=body)
    return res