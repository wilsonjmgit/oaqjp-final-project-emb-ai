import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    # The value being returned must be the text attribute of the response object as received from the Emotion Detection function.
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        # Example emotion_predictions = {'anger': 0.029103195, 'disgust': 0.0067921067, 'fear': 0.027528232, 'joy': 0.876574, 'sadness': 0.06151191}
        # emotion_predictions is already a dictionary similar to the requested output format.  Just need to add dominant_emotion.
        dominant_emotion = max(emotion_predictions, key = emotion_predictions.get)
        emotion_predictions['dominant_emotion'] = dominant_emotion
        return emotion_predictions
    elif response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        return None
