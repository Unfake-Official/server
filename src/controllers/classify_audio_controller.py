from flask import Request, jsonify
from src.controllers.validators.classify_request_validator import classify_request_validator
from src.http.error_handler import handle_error
from src.business.classify_audio_use_case import classify_audio_use_case


def classify(request: Request):
    try:
        classify_request_validator(request)

        audio = request.files['audio']

        inference = classify_audio_use_case(audio)

        return jsonify(inference)
    except Exception as error:
        print(error.with_traceback())
        response = handle_error(error)
        return jsonify(response.body), response.status_code
