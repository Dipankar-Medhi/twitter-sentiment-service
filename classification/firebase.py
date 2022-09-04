import requests
import os
import json


class Firebase:
    def __init__(self) -> None:
        pass

    def getTweetsFromAPI(self):
        tweets = requests.get("http://api:8000/tweets")
        result = tweets.json()["tweets"]
        print("Tweets loaded for classification!")
        print("-" * 30)

        return result

    def sendSentimentsToAPI(self, sentiments):
        res = requests.post("http://api:8000/sentiments", data=sentiments)
        return res.json()
