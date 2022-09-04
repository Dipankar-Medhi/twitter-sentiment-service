from fastapi import FastAPI
from firebase import Firebase
import firebase_admin

app = FastAPI()
firebase = Firebase()
# connect firebase db


@app.get("/")
def home():
    return {"message": "Sentiments"}


@app.get("/sentiments")
async def sentiments():
    ref, firebae_app = firebase.connect()
    sentiments = firebase.getSentimentsFromDB(ref)
    firebase_admin.delete_app(firebae_app)
    print("Firebase app deleted!")
    return {"sentiments": sentiments}

@app.post("/sentiments")
async def sendSentiments(data: dict):
    ref, firebase_app = firebase.connect()
    firebase.setSentimentsToDB(ref.child("sentiments"), data)
    firebase_admin.delete_app(firebase_app)
    return {"message": "sentiments stored successfully"}


@app.get("/tweets")
async def tweets():
    ref, firebase_app = firebase.connect()
    tweets = firebase.getTweetsFromDB(ref)
    firebase_admin.delete_app(firebase_app)
    print("Firebase app deleted!")
    return {"tweets": tweets}


@app.post("/tweets")
async def sendTweets(data: dict):
    ref, firebase_app = firebase.connect()
    firebase.storeTweetsOnDB(ref.child("tweets"), data)
    firebase_admin.delete_app(firebase_app)
    return {"message": "tweets stored successfully"}
