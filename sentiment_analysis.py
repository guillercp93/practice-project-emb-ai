import requests

URL = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
HEADERS = {
    "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
}


def sentiment_analyzer(text_to_analyse):
    response = requests.post(
        URL,
        json={"raw_document": {"text": text_to_analyse}},
        headers=HEADERS
    )

    return response.text
