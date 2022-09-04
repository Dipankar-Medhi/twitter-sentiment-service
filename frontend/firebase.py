import requests
import os
import json


class Firebase:
    def __init__(self) -> None:
        pass

    def getSentimentsFromDB(self):
        tweets = requests.get("http://api:8000/sentiments")
        result = tweets.json()["sentiments"]
        print(result)
        return result
