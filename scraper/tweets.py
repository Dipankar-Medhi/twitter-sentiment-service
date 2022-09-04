from datetime import date, timedelta
from firebase import Firebase
from scraper import Scraper
import json
from omegaconf import OmegaConf

config = OmegaConf.load("./config/config.yml")

scraper = Scraper()
firebase = Firebase()


def tweetToDB():
    enddate = date.today()
    startdate = date.today() - timedelta(days=3)
    print(enddate, startdate)

    # companies = ["Apple", "Facebook", "Microsoft"]
    companies = config["input-config"]["companies"]
    print(companies)
    print("-" * 30)
    final_tweets = {}
    print("Scrapping tweets ...")
    print("-" * 30)

    for company in companies:
        query = f"{company} (@{company}) lang:en until:{enddate} since:{startdate}"

        scraper = Scraper()
        final_tweets[company] = scraper.get_tweets(query)

    result = json.dumps(final_tweets)
    print("Scrapping done!")
    print("-" * 30)

    # send data to firebase
    res = firebase.send_tweets_api(result)
    return res
