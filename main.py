from typing import Union

from fastapi import FastAPI
from es.es_utils import save_to_es

app = FastAPI()


@app.get("/")
def read_root():
    return {"Status": "Server is up and running"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


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