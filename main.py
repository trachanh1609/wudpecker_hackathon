from typing import Union, List

from fastapi import FastAPI
from es import es_utils
from models.search_models import SearchItem

app = FastAPI()


@app.get("/")
def read_root():
    return {"Status": "Server is up and running"}



# @app.post("/calls/")
# async def create_calls(data: dict):
#     response = {}
#     try:
#         save_to_es(data)
#         response = {
#             "status": "success",
#             "message": "Data saved successfully",
#             "data": data
#         }
#     except Exception as e:
#         print(e)
#         response = {
#             "status": "error",
#             "message": "Data was not saved"
#         }

#     return response

@app.post("/calls/search")
async def search_calls(data: SearchItem):
    response = {}
    try:
        res = es_utils.search_from_es(data)
        response = {
            "total": res['hits']['total']['value'],
            "page": data.page,
            "page_size": data.page_size,
            "results": [hit['_source'] for hit in res['hits']['hits']]
        }
    except Exception as e:
        print(e)
        response = {
            "status": "error",
            "message": "Request was not valid"
        }

    return response