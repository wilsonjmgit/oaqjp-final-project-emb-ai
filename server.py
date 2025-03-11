'''
server.py to run a server to input textToAnalyze and output emotion analysis response
'''
# Import libraries
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Instantiate Flask functionality
app = Flask(__name__)

@app.route("/")
def render_index_page():
    '''
    Function to render index.html page
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
# Need a different name, not 'emotion_detector' so it doesn't clash
def emotions_detector():
    '''
    Function to call emotion_detector with argument 'textToAnalyze',
    return the emotions dictionary emotions_dict, and
    format the output as requested. 
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    emotions_dict = emotion_detector(text_to_analyze)
    # Get the dominant emotion, and remove it from emotions_dict
    dominant_emotion = emotions_dict.pop('dominant_emotion', None)
    no_brackets_text = str(emotions_dict).replace(r'{','').replace(r'}','')
    emotions_text = f"For the given statement, the system response is {no_brackets_text}.\
      The dominant emotion is {dominant_emotion}."
    if dominant_emotion is not None:
        return emotions_text
    return "Invalid text! Please try again!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
