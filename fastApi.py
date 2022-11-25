from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
# import json
import json, requests
from fastapi.responses import JSONResponse



app = FastAPI()


# this programm will be API server

# https://www.georisques.gouv.fr/api/v1/gaspar/catnat
PATH = "https://www.georisques.gouv.fr/"


# get the data from the API
@app.get("/get_datas_AZI")
async def get_data(code_insee: str, range: int = 100, page : int = 1,page_size : int = 10):
    """
    --AZI--
     def :Opérations sur les Atlas des Zones Inondables (AZI)
    get the data from the API

    args:
        code_insee (str): the code of the city
        range (str): the range of the data
        page (int): the page of the data
        page_size (int): the size of the page
    """
    # get the data from the API
    url = PATH + "api/v1/gaspar/catnat"
    if(len(code_insee) != 5):
        return JSONResponse(status_code=404, content={"message": "code_insee is not valid"})
    params = {
        "code_insee": code_insee,
        "range": range,
        "page": page,
        "page_size": page_size
    }
    response = requests.get(url, params=params)
    data=response.json()
    return data.get("data")
    
    

@app.get("/get_datas_catnat")
async def get_datas_catnat(code_insee: str, range: int = 100, page : int = 1,page_size : int = 10):
    """
    --catnat--
    def :Opérations sur les données de catastrophes naturelles
    args:
        code_insee (str): the code of the city
        range (str): the range of the data
        page (int): the page of the data
        page_size (int): the size of the page
    """
    url = PATH + "api/v1/gaspar/catnat"
    response = requests.get(url)
    data=response.json()
    return data.get("data")




if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)