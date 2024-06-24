from src.http.response import HttpResponse
from src.http.errors.bad_request import BadRequest

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, BadRequest):
        return HttpResponse(
            status_code = error.status_code,
            body = {
                'error': [{
                    'title': error.name,
                    'details': error.message
                }]
            }
        )

    return HttpResponse()
