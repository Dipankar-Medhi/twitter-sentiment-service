from scipy.special import softmax
from model import Model
import numpy as np


class Classifier:
    """A class that prepares the model for inferencing."""

    def __init__(self) -> None:
        self.roberta_tokenizer = Model.load_tokenizer()
        self.roberta_model = Model.load_model()

    def get_sentiment(self, text):
        """Generates sentiments from the input text.

        Args:
            text (string): input string whose sentiments is to be found.

        Returns:
            string: sentiment of the input text.
        """
        labels = ["negative", "neutral", "positive"]
        encoded_input = self.roberta_tokenizer(text, return_tensors="pt")
        output = self.roberta_model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        return str(labels[ranking[0]])

    def get_sentiment_score(self, text):
        """Generates the score of the sentiments calculated.

        Args:
            text (string): input text.

        Returns:
            float: score of the sentiment
        """
        encoded_input = self.roberta_tokenizer(text, return_tensors="pt")
        output = self.roberta_model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        result = float(scores[ranking[0]])
        return np.round(result, 4)
