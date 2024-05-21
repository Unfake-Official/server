from cerberus import Validator
from werkzeug.datastructures import FileStorage

from src.types.errors.bad_request import BadRequest

def classify_audio_validator(request: any) -> None:
    schema = Validator({
        'audio': {
            # 'type': FileStorage,
            'required': True
        }
    })

    response = schema.validate(request.files)
    if response is False:
        raise BadRequest(schema.errors)
