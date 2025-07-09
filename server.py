"""Flask web server for emotion detection."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main HTML page with input form."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """Handle emotion detection logic and return formatted output or error."""
    text = request.args.get('textToAnalyze')  # Get the input from the query string
    result = emotion_detector(text)

    # Error handling for blank input or 400 status from Watson API
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Create response string for display
    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_str

if __name__ == '__main__':
    app.run(debug=True)
    
