from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detector Running"

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get('textToAnalyze')

    if not text:
        return "Invalid input! Please enter text."

    result = emotion_detector(text)

    if result is None:
        return "Error processing request."

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)