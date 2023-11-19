from pydantic import BaseModel
from typing import Union, List

class SearchItem(BaseModel):
    search_query: Union[str, None] = ''
    file_names: List[Union[str, None]] = []
