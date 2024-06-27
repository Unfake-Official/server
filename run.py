from src.server import app
from waitress import serve

mode = 'dev'

host = '0.0.0.0'
port = 8080

if __name__ == '__main__':
    if mode == 'dev':
        app.run(host = host, port = port, debug = True)
    else:
        serve(app, host = host, port = port, threads = 5)
