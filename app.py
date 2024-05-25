from flask import Flask, request, jsonify
from googletrans import Translator
import json
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    dest_lang = data.get('lang')
    if text and dest_lang:
        translation = translator.translate(text, dest=dest_lang)
        return jsonify({'translated_text': translation.text})
    return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default to port 10000 if PORT is not set
    app.run(host='0.0.0.0', port=port, debug=True)