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

    # Print the response for debugging
    print("Response Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())  # Print the full JSON response
    except Exception as e:
        print("Error parsing JSON response:", e)
        print("Response Text:", response.text)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the full response JSON for now
        return response.json()
    else:
        # Handle errors
        return f"Error: {response.status_code}, {response.text}"