from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze/<text>', methods=['GET'])
def analyze(text):
    # Mock sentiment analysis logic
    positive_words = ['fantastic', 'great', 'excellent', 'amazing', 'good', 'happy']
    negative_words = ['bad', 'terrible', 'horrible', 'poor', 'sad', 'unhappy']
    
    text_lower = text.lower()
    
    if any(word in text_lower for word in positive_words):
        sentiment = 'positive'
    elif any(word in text_lower for word in negative_words):
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
        
    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
