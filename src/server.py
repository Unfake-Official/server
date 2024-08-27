from flask import Flask, request, jsonify
from flask_cors import CORS
from src.controllers.classify_audio_controller import classify

app = Flask(__name__)
CORS(app)

@app.route('/classify', methods = ['POST'])
def classify_audio():
    return classify(request = request)
