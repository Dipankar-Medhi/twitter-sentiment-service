import snscrape.modules.twitter as sntwitter
import re
import json


class Scraper:
    """A class to scrape tweets."""

    def __init__(self) -> None:
        self.tweet_list = []

    def __preprocess_tweets(self, tweet):
        """Preprocess tweets"""
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

    def get_tweets(self, query):
        """Get tweets based on Advanced search query."""
        tweets = sntwitter.TwitterSearchScraper(query).get_items()

        for tweet in tweets:
            tweets = {}
            tweets["tweet"] = self.__preprocess_tweets(tweet.content)
            tweets["date"] = f"{tweet.date.year}-{tweet.date.month}-{tweet.date.day}"
            if len(self.tweet_list) == 100:
                break
            self.tweet_list.append(tweets)

        return self.tweet_list
