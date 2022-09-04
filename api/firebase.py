import firebase_admin
from firebase_admin import db
from dotenv import load_dotenv
import os

load_dotenv()


credentials = {
    "type": "service_account",
    "project_id": "tweetsgrabber",
    "private_key_id": f"{os.getenv('PRIVATE_KEY_ID')}",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCnq3orQfxrcay0\nllFOnMpevrPT/Q83T7AzpY4BgG2kkChmOqjmL/6zOhnT0lzALQR4qKxa7f/91BVB\nE0+4zraxUg9WoD/nm3uM02mfaTKWGDxixwb7LKeJWOIT3Lz1R/2Q73kQR+dhBMhZ\nHdZ4Q6VF+iaJ47DY2LJXc4A8Lw1+3umflQ3chzUiMPV90Ny6hrJ9LLMuBKSuo1nc\nVTK0maLeuLLOTvf0Yd2snhbhEtOl7IXghNDEC3oxdzAd/cCSwWCD1kXIZfLEjqgw\nXAVyz+UliAvWIAfmhKSF+zTbD3dBIyMkpsjqmMlvsLnVqxuiyokItiQ5fLhceUuM\nPEzySblVAgMBAAECggEAAIT0dOvYZ1DL0ydgCxlLOy3mCrMO+AHkLtTFctW+ATN9\nHIvz9/qQFGgKqnBNXz8Ec4c6OXHhSBz/D9uKdK0XPcdeSstmR0ZhBJenDRpbUMG0\ndi3dpKuHvVIsKRmW8D+P1oIXYuiGG/PS1wvTnT3AZk4XDnhJFPLe4ox2CjmvFgSD\ndJlMpoJ1eZgyq3SdL4ie746YsQn+nBiI69Mdzzai8m0rP5Ws134EblKlcyTyRNNm\nXGIcYQNZpuPm/X6s0ZiNcGp5S2fO2TESBTEJdbIsLLLf0yAdjBm36YOyHMgHfr23\n8/UxhRw+IWyOk/MEpAGucI5uI/58rLC7Jf1Ol1ce4QKBgQDkcYP4xSnwZukJrbKP\n+monOozVtr2OMFcaHUhlddoG5cUvjmIN829RVBwgL1YEkJ5qJ516u+tiG/d+6xNl\nm/G6ERwA+SZksmTX6n9WMoEJvq6tJkZEsMyASBVCkEUk9nFGDQMa8YkOSuIf4zyq\nsamlluexlekL0GjS7YX3TaEkmQKBgQC75TulGHzQpP5x7MP0SdBJdahhFAxChGvB\nLz0vMZNE4NgtzoY6gH6gGBhRwaHOHAdAkTcVj2cjIWkkt8BYGadAVxf0QJ3Q6KZk\nwB1wiKdLzO9oxqAqWLHR+ktNv+R0oXCsUXbwbWFlz3KKLPNfQW6DTWYo9gRUDC7w\nxn4dVtW0HQKBgE3m/BdAvU2S+pNnXYZF4h9gkxhqSfgMOhfYtpCLAP/rKTRPfNa/\nFk4IvdKn8dB6tNsEiWqKXPnHCb6JUcMLzAIkxYT7cgFS6JrNCAGQFXsKQK0haUMR\ne5ufeUiKxFmXhQdbdpygk5mBJd2z80NOdMjYTki8E44I00Zi45VzLqm5AoGAZGrJ\nap1gr11OgvJHc3ozb98Kov9E4hPFRtSJPXygOTJ1Nl3mjMN5aPQXozH52J5QHei9\n6K7gLv0/JRlzGWJ0aUViju4tqaV8r+GgmjDeP/uBg5yLorYOKqs6rY29ebuB7QYI\nq8u5PuEUVNZbJvBgMJof3ApHG+f6+kEKy4FJ6t0CgYAmtFlGi8AOHy9lXKOXljtl\n5U3XUl8j6h+JsZjZnNweHM4ufb7NFQ7fqY7tyTiZAp8274LQmkRfumEs825DGTib\n1PgG1bq3kFD0LISgdG1p1kX07a2EuLQ+cW9tsAqb538vL8BHWsZmaNOlL0L3pIqq\n98/lWWjFpwAVCr5h9lOE+g==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-99cy7@tweetsgrabber.iam.gserviceaccount.com",
    "client_id": "116748516696399509624",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-99cy7%40tweetsgrabber.iam.gserviceaccount.com",
}


class Firebase:
    def __init__(self) -> None:
        pass

    def connect(self):
        """Connect to the database."""
        cred = firebase_admin.credentials.Certificate(credentials)
        app = firebase_admin.initialize_app(
            cred, {"databaseURL": "https://tweetsgrabber-default-rtdb.firebaseio.com/"}
        )
        print("Connected!")
        ref = db.reference("/")
        return ref, app

    def getSentimentsFromDB(self, ref):
        """Get the sentiments from the database.

        Args:
            ref : reference to the database.

        Returns:
            sentiments : sentiments
        """
        sentiments = ref.child("sentiments").get()
        return sentiments

    def getTweetsFromDB(self, ref):
        tweets = ref.child("tweets").get()
        return tweets

    def storeTweetsOnDB(self, ref, data):
        """Store data into the firebase database."""
        ref.set(data)

    def setSentimentsToDB(self, ref, sentiments):
        """Store sentiments data in the database."""
        ref.set(sentiments)
