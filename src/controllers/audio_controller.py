from flask import Blueprint, request, jsonify

audio_routes_blueprint = Blueprint('audio_routes', __name__)

@audio_routes_blueprint.route('/classify', methods = ['POST'])
def classify_audio():
    body = request.json
    shit = body.get('what')
    print(shit)

    return jsonify({ 'response': 'Hello World!' })
