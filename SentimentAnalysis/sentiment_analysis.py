"""
sentiment_analysis.py

This module provides functionality to analyze the sentiment of text using
an external sentiment analysis service.
It includes the `sentiment_analyzer` function, which sends a request to
the service and returns the analysis results.
"""

import json
import requests

URL = (
    'https://sn-watson-sentiment-bert.labs.skills.network/v1/'
    'watson.runtime.nlp.v1/NlpService/SentimentPredict'
)
HEADERS = {
    "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
}


def sentiment_analyzer(text_to_analyse):
    """
    Analyzes the sentiment of the provided text using an external sentiment analysis service.

    Args:
        text_to_analyse (str): The text input for which sentiment analysis is to be performed.

    Returns:
        dict: A dictionary containing the sentiment analysis results, parsed from the JSON response
              of the external service.

    Raises:
        RequestException: If the request to the sentiment analysis service fails.
    """
    response = requests.post(
        URL,
        json={"raw_document": {"text": text_to_analyse}},
        headers=HEADERS,
        timeout=10
    )

    return json.loads(response.text)
