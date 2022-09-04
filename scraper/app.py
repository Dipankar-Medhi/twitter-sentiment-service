from tweets import tweetToDB
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI

app = FastAPI()


def addtweets():
    print("adding tweets to DB!")
    res = tweetToDB()
    print(res)


addtweets()
print("Tweets added!")
print("-" * 30)


@app.get("/")
def home():
    return "Adding tweets to DB on the background once a month."


# tweets scrapping schedular
scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(addtweets, "interval", minutes=10080)
scheduler.start()
