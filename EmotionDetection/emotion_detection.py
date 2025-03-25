import requests

def emotion_detector(text_to_analyze):
    # Define the URL and headers for the Watson NLP Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Define the input JSON payload
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send a POST request to the Watson NLP API
    response = requests.post(url, headers=headers, json=input_json)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        response_data = response.json()

        # Extract the overall emotion scores
        emotion_predictions = response_data.get("emotionPredictions", [])
        if emotion_predictions:
            overall_emotions = emotion_predictions[0].get("emotion", {})

            # Find the dominant emotion
            dominant_emotion = max(overall_emotions, key=overall_emotions.get)

            # Format the output
            formatted_output = {
                'anger': overall_emotions.get('anger', 0),
                'disgust': overall_emotions.get('disgust', 0),
                'fear': overall_emotions.get('fear', 0),
                'joy': overall_emotions.get('joy', 0),
                'sadness': overall_emotions.get('sadness', 0),
                'dominant_emotion': dominant_emotion
            }
            return formatted_output
        else:
            return "No emotion predictions found in response."
    else:
        # Handle errors
        return f"Error: {response.status_code}, {response.text}"