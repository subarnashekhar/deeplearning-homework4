#!/usr/bin/env python3
"""Demonstrate a basic NLP preprocessing pipeline."""

import re

from nltk.stem import PorterStemmer


SENTENCE = "NLP techniques are used in virtual assistants like Alexa and Siri."
STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "to",
    "was",
    "were",
    "with",
}


def preprocess(sentence: str) -> tuple[list[str], list[str], list[str]]:
    """Return the original tokens, filtered tokens, and stemmed tokens."""
    # Toknize words and punctation without Punkt downloads.
    tokens = re.findall(r"\b\w+\b|[^\w\s]", sentence)

    # Remuve stopwords while keeping punctation tokens.
    filtered_tokens = [
        token for token in tokens if token.casefold() not in STOP_WORDS
    ]

    # Apply Porter steming to the remaning words.
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token.casefold()) for token in filtered_tokens]

    return tokens, filtered_tokens, stemmed_tokens


def main() -> None:
    original_tokens, filtered_tokens, stemmed_tokens = preprocess(SENTENCE)

    print("Original Tokens:", original_tokens)
    print("Tokens Without Stopwords:", filtered_tokens)
    print("Stemmed Words:", stemmed_tokens)


if __name__ == "__main__":
    main()
