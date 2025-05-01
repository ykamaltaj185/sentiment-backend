from flask import Flask, request, jsonify
from flask_cors import CORS
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

app = Flask(__name__)
CORS(app)

sid = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return 'Sentiment Analysis Backend is Running!'

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text', '')
    score = sid.polarity_scores(text)
    sentiment = 'neutral'
    if score['compound'] >= 0.05:
        sentiment = 'positive'
    elif score['compound'] <= -0.05:
        sentiment = 'negative'
    return jsonify({'sentiment': sentiment, 'score': score})

if __name__ == '__main__':
    print("Starting backend...")
    app.run(debug=True)
