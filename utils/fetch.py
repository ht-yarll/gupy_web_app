import json

import requests


def fetchdata(label: str) -> dict:
    url = f"https://portal.api.gupy.io/api/job?name={label}&offset=0&limit=400"

    r = requests.get(url)
    response = r.json()
   
    return response