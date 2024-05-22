from flask import Blueprint, request, jsonify
from pydub import AudioSegment
from src.controllers.validators.classify_audio_validator import classify_audio_validator
from src.types.errors.bad_request import BadRequest
from src.types.http.response import HttpResponse
from src.business.classify_audio_use_case import ClassifyAudioUseCase
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as img





audio_routes_blueprint = Blueprint('audio_routes', __name__)

@audio_routes_blueprint.route('/api/audio/classify', methods = ['POST'])
def classify_audio():
    try:
        # classify_audio_validator(request)

        audio = request.files['audio']

        nome = audio.filename

        filename = os.path.join(uploads_folder, nome)
        audio.save(filename)

        audio = AudioSegment.from_file(filename)

        y, sr = librosa.load(filename)

        C = np.abs(librosa.cqt(y, sr=sr))
        C = librosa.amplitude_to_db(C, ref=np.max)

        output_folder = os.path.join(uploads_folder, 'outputs')
        image_output = os.path.join(output_folder, 'teste.png')

        print(image_output)

        plt.imsave(image_output, C, cmap='gray')
        image = img.open(image_output)
        new_image = image.resize((256, 256))
        new_image.save(image_output)

        # response = ClassifyAudioUseCase().classify(audio)

        return jsonify('1')
    except Exception as error:
        # if isinstance(error, BadRequest):
        #     return HttpResponse(
        #         status_code = error.status_code,
        #         body = {
        #             'error': [{
        #                 'title': error.name,
        #                 'details': error.message
        #             }]
        #         }
        #     )
        # else:
        #     return HttpResponse()
        return jsonify('1'), 400
