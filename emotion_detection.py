import requests
import json

def emotion_detector(text_to_analyse):
    ENDPOINT = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    PAYLOAD = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(ENDPOINT, headers = HEADERS, json = PAYLOAD)
    res = response.json()
    # print(json.dumps(response.json(), indent = 4))
    res = res['emotionPredictions'][0]['emotion']
    dominant_emotion = max(res, key=res.get)
    dominant_emotion_value = res[dominant_emotion]
    res["dominant_emotion"] = dominant_emotion
    # return response.text
    return res

# emotion_detector("hello how are you?")
