from cerberus import Validator
from werkzeug.datastructures.file_storage import FileStorage

from src.http.errors.bad_request import BadRequest


def is_filestorage(field, value, error):
    if not isinstance(value, FileStorage):
        error(field, '"audio" field must be a FileStorage instance')


def classify_audio_validator(request: any) -> None:
    schema = Validator({
        'audio': {
            'required': True,
            'check_with': is_filestorage
        }
    })

    response = schema.validate(request.files)
    if response is False:
        raise BadRequest(schema.errors)
