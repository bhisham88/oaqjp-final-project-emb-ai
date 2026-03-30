from flask import Flask
import emotion_detection
import json

app = Flask(__name__)

# USER_MESSAGE = "I love my life"
USER_MESSAGE = "I think I am having fun"

@app.route("/emotionDetector")
def emotion_detector():
    response = emotion_detection.emotion_detector(USER_MESSAGE)
    anger = str(response.get("anger"))
    disgust = str(response.get("disgust"))
    fear = str(response.get("fear"))
    joy = str(response.get("joy"))
    sadness = str(response.get("sadness"))
    dominant_emotion = str(response.get("dominant_emotion"))
    response_message = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    return response_message

if __name__ == "__main__":
    app.run(debug=True)