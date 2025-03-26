"""
Flask application for emotion detection using Watson NLP.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Endpoint to detect emotions in a given statement.

    Returns:
        JSON response with emotion scores and dominant emotion,
        or an error message if the input is invalid.
    """
    # Get the input statement from the request
    data = request.get_json()

    # Ensure the 'statement' key exists in the request JSON
    if not data or "statement" not in data:
        return jsonify({"error": "No statement provided"}), 400

    # Get the statement value (even if it's blank)
    statement = data.get("statement", "")

    # Call the emotion_detector function
    result = emotion_detector(statement)

    # Check if the dominant emotion is None
    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"})

    # Format the response
    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response})

if __name__ == '__main__':
    # Main entry point for the Flask application
    app.run(host='localhost', port=5000)
