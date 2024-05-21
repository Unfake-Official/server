from flask import Blueprint, request, jsonify

from src.infrastructure.spectrogram_handler import SpectrogramHandler
from src.infrastructure.inference_handler import InferenceHandler

audio_routes_blueprint = Blueprint('audio_routes', __name__)

@audio_routes_blueprint.route('/api/audio/classify', methods = ['POST'])
def classify_audio():
    try:
        audio = request.files['audio']
        audio_name = audio.filename

        print(audio_name)

        spectrogram_creator = SpectrogramHandler()
        spec = spectrogram_creator.create_spectrogram(audio_name)

        inference_handler = InferenceHandler()
        inference = inference_handler.inference(spec)

        return jsonify(inference)
    except:
        return jsonify({ 'status': 'bad request' })
