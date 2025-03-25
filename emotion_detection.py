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

    # Print the response for debugging
    print("Response Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())  # Print the full JSON response
    except Exception as e:
        print("Error parsing JSON response:", e)
        print("Response Text:", response.text)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        response_data = response.json()

        # Extract the overall emotion scores
        emotion_predictions = response_data.get("emotionPredictions", [])
        if emotion_predictions:
            overall_emotions = emotion_predictions[0].get("emotion", {})
            # Find the emotion with the highest score
            most_prominent_emotion = max(overall_emotions, key=overall_emotions.get)
            return {
                "most_prominent_emotion": most_prominent_emotion,
                "score": overall_emotions[most_prominent_emotion]
            }
        else:
            return "No emotion predictions found in response."
    else:
        # Handle errors
        return f"Error: {response.status_code}, {response.text}"