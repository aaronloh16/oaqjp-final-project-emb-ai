"""
This module sets up a Flask web server for an emotion detection application.
It provides routes for rendering the web interface and for handling
emotion detection requests.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_api():
    """
    Handles the GET request for emotion detection.
    Retrieves the text to analyze from the request, passes it to the emotion detector,
    and returns the formatted response.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Extract the emotion scores and dominant emotion from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format the response string
    formatted_response = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return formatted_response


@app.route("/")
def render_index_page():
    """
    Renders the index.html template for the web interface.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
