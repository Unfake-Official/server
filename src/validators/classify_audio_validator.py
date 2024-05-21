from cerberus import Validator
from werkzeug.datastructures import FileStorage

from src.types.errors.bad_request import BadRequest

def classify_audio_validator(request: any) -> None:
    file_validator = Validator({
        'audio': {
            'type': FileStorage,
            'required': True,
            'empty': False
        }
    })

    response = file_validator.validate(request.files)
    if response is False:
        raise BadRequest(file_validator.errors)
