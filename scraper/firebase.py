import requests


class Firebase:
    def __init__(self) -> None:
        pass

    def send_tweets_api(self, tweets):
        res = requests.post("http://api:8000/tweets", data=tweets)
        return res.json()
