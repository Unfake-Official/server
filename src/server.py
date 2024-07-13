from flask import Flask
from flask_cors import CORS
from src.controllers.audio_controller import audio_routes_blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(audio_routes_blueprint)
