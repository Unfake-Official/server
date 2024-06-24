from typing import Dict

class HttpResponse:
    def __init__(self, status_code: int = 500, body: Dict = None) -> None:
        if body is None:
            body = {
                'error': [{
                    'title': 'Internal Server Error',
                    'details': 'An error occured when trying to perform the specified operation. Try again later.'
                }]
            }
        self.status_code = status_code
        self.body = body
