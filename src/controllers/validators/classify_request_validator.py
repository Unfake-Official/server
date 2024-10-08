from flask import Request
from src.http.errors.bad_request import BadRequest


def classify_request_validator(request: Request) -> None:
    if not request.files:
        raise BadRequest("No file was provided in the request.")

    if 'audio' not in request.files or request.files['audio'] is None:
        raise BadRequest("No file named 'audio' was provided in the request.")
