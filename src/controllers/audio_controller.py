from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from src.infrastructure.spectrogram_handler import SpectrogramHandler
from src.infrastructure.inference_handler import InferenceHandler

from src.validators.classify_audio_validator import classify_audio_validator

audio_routes_blueprint = Blueprint('audio_routes', __name__)

@audio_routes_blueprint.route('/api/audio/classify', methods = ['POST'])
def classify_audio():
    response = None
    try:
        audio = request.files['audio'] # type => FileStorage
        audio_name = audio.filename

        response = classify_audio_validator

        print(audio_name)

        spectrogram_creator = SpectrogramHandler()
        spec = spectrogram_creator.create_spectrogram(audio_name)

        inference_handler = InferenceHandler()
        inference = inference_handler.inference(spec)

        return jsonify(inference)
    except:
        return jsonify({ 'status': 'bad request' })
