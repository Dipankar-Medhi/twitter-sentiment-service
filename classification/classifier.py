from scipy.special import softmax
from model import Model
import numpy as np


class Classifier:
    """A class that deals with sentiment analysis."""

    def __init__(self) -> None:
        self.roberta_tokenizer = Model.load_tokenizer()
        self.roberta_model = Model.load_model()

    def get_sentiment(self, text):
        """A method to get the sentiment of a piece of text."""
        labels = ["negative", "neutral", "positive"]
        encoded_input = self.roberta_tokenizer(text, return_tensors="pt")
        output = self.roberta_model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        return str(labels[ranking[0]])

    def get_sentiment_score(self, text):
        """A method to get the score of the sentiment analysis."""
        encoded_input = self.roberta_tokenizer(text, return_tensors="pt")
        output = self.roberta_model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        result = float(scores[ranking[0]])
        return np.round(result, 4)
