import firebase_admin
from firebase_admin import db
from dotenv import load_dotenv
import os

load_dotenv()



class Firebase:
    def __init__(self) -> None:
        pass

    def connect(self):
        """Connect to the database."""
        cred = firebase_admin.credentials.Certificate("<path-to-firebase-api-key.json>")
        app = firebase_admin.initialize_app(
            cred, {"databaseURL": "<database-url>"}
        )
        print("Connected!")
        ref = db.reference("/")
        return ref, app

    def getSentimentsFromDB(self, ref):
        """Get the sentiments from the database.

        Args:
            ref : reference to the database.

        Returns:
            sentiments : user sentiments
        """
        sentiments = ref.child("sentiments").get()
        return sentiments

    def getTweetsFromDB(self, ref):
        """Request tweeets from the databse.

        Args:
            ref : reference to the tweets database.

        Returns:
            tweets: tweets from the database.
        """
        tweets = ref.child("tweets").get()
        return tweets

    def storeTweetsOnDB(self, ref, data):
        """Save the tweets on the databse.
        """
        ref.set(data)

    def setSentimentsToDB(self, ref, sentiments):
        """Store sentiments data in the database."""
        ref.set(sentiments)
