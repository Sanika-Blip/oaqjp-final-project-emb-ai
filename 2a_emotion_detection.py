"""Emotion detection using the Watson NLP library (Task 2)."""
import requests

URL = ('https://sn-watson-emotion.labs.skills.network/v1/'
       'watson.runtime.nlp.v1/NlpService/EmotionPredict')
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyse):
    """Send text to the Watson Emotion service and return the raw response text."""
    input_json = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(URL, json=input_json, headers=HEADERS, timeout=10)
    return response.text
