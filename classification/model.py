from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from pathlib import Path
import os


class Model:
    """A model class to load the model and tokenizer."""

    def __init__(self) -> None:
        pass

    def load_model():
        """Load the classfication model"""
        model = AutoModelForSequenceClassification.from_pretrained(
            "models/roberta-base/"
        )
        return model

    def load_tokenizer():
        """Load the classification tokenizer."""
        tokenizer = AutoTokenizer.from_pretrained("models/roberta-base/")
        return tokenizer
