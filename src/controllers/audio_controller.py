from flask import Blueprint, request, jsonify
from src.controllers.validators.classify_audio_validator import classify_audio_validator
from src.http.error_handler import handle_error
from src.business.classify_audio_use_case import ClassifyAudioUseCase

audio_routes_blueprint = Blueprint('audio_routes', __name__)

@audio_routes_blueprint.route('/api/audio/classify', methods = ['POST'])
def classify_audio():
    try:
        classify_audio_validator(request)

        audio = request.files['audio']

        classify_audio_use_case = ClassifyAudioUseCase()
        inference = classify_audio_use_case.classify(audio)

        return jsonify(audio.filename)
    except Exception as error:
        response = handle_error(error)
        return jsonify(response.body), response.status_code
