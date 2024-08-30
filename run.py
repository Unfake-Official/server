import os
from src.server import app
from waitress import serve
from dotenv import load_dotenv

host = '0.0.0.0'

load_dotenv()
environment = os.environ.get('ENVIRONMENT', 'production')

if __name__ == '__main__':
    if environment == 'development':
        app.run(host = host, debug = True)
    else:
        serve(app, host = host, port = 8080, threads = 5)
