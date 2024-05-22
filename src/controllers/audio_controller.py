from flask import Blueprint, request, jsonify
from pydub import AudioSegment
from src.controllers.validators.classify_audio_validator import classify_audio_validator
from src.types.errors.bad_request import BadRequest
from src.types.http.response import HttpResponse
from src.business.classify_audio_use_case import ClassifyAudioUseCase
import os


uploads_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
if not os.path.exists(uploads_folder):
    os.makedirs(uploads_folder)


audio_routes_blueprint = Blueprint('audio_routes', __name__)

@audio_routes_blueprint.route('/api/audio/classify', methods = ['POST'])
def classify_audio():
    try:
        # classify_audio_validator(request)

        audio = request.files['audio']
        print("-------")
        filename = os.path.join(uploads_folder, audio.filename)
        audio.save(filename)

        # Manipular o arquivo (exemplo: converter para wav)
        audio = AudioSegment.from_file(filename)


        #response = ClassifyAudioUseCase().classify(audio)

        return jsonify('1')
    except Exception as error:
        # if isinstance(error, BadRequest):
        #     return HttpResponse(
        #         status_code = error.status_code,
        #         body = {
        #             'error': [{
        #                 'title': error.name,
        #                 'details': error.message
        #             }]
        #         }
        #     )
        # else:
        #     return HttpResponse()
        return jsonify('1'), 400
