from flask import Blueprint, request, jsonify

from src.controllers.validators.classify_audio_validator import classify_audio_validator

from src.types.errors.bad_request import BadRequest
from src.types.http.response import HttpResponse

from src.business.classify_audio_use_case import ClassifyAudioUseCase

audio_routes_blueprint = Blueprint('audio_routes', __name__)

@audio_routes_blueprint.route('/api/audio/classify', methods = ['POST'])
def classify_audio():
    try:
        classify_audio_validator(request)

        audio = request.files['audio']

        response = ClassifyAudioUseCase().classify(audio)

        return jsonify(response)
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
