from flask import Flask
from src.controllers.audio_controller import audio_routes_blueprint

app = Flask(__name__)

app.register_blueprint(audio_routes_blueprint)
