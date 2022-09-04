from firebase import Firebase
from classifier import Classifier
from fastapi import FastAPI
import re
import json
from apscheduler.schedulers.background import BackgroundScheduler

firebase = Firebase()
classifier = Classifier()
app = FastAPI()
print("Model loaded!")


def preprocess_tweets(tweet):
    tweet = re.sub("(@[A-Za-z]+[A-Za-z0-9-_]+)", "", tweet)
    tweet = re.sub(r"http\S+", "", tweet)  # remove http links
    tweet = re.sub(r"bit.ly/\S+", "", tweet)  # remove bitly links
    html = re.compile("<.*?>")
    tweet = html.sub(r"", tweet)
    tweet = re.sub("([_]+)", "", tweet)
    email = re.compile(r"[\w\.-]+@[\w\.-]+")
    tweet = email.sub(r"", tweet)
    tweet = "".join(i for i in tweet if ord(i) < 128)
    tweet = tweet.lower()
    return tweet


def sentiments():
    all_sentiments = {}
    tweets = firebase.getTweetsFromAPI()
    print("Got the tweets From DB")
    companies = [key for key, _ in tweets.items()]
    print(companies)
    print("-" * 30)
    pos_count = 0
    neg_count = 0
    neu_count = 0
    total_count = 0
    for company in companies:
        for data in tweets[company]:
            sentiment = classifier.get_sentiment(data["tweet"])
            # tweet_list.append(classifier.get_sentiment(data['tweet']))
            total_count += 1
            if sentiment == "positive":
                pos_count += 1
            elif sentiment == "negative":
                neg_count += 1
            else:
                neu_count += 1
        all_sentiments[company] = {
            "positive": round((pos_count / total_count) * 100, 2),
            "negative": round((neg_count / total_count) * 100, 2),
            "neutral": round((neu_count / total_count) * 100, 2),
        }

    return all_sentiments


def set_sentiments(sentiments):
    res = firebase.sendSentimentsToAPI(sentiments)
    return res


def add_sentiments():
    results = sentiments()
    results = json.dumps(results)
    response = set_sentiments(results)

    # print("Sentiments added to DB")


add_sentiments()
print("Sentiments added!")
print("-" * 30)


@app.get("/")
def home():
    return {"message": "Classification of tweets in progress..."}


scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(add_sentiments, "interval", minutes=10180)
scheduler.start()
