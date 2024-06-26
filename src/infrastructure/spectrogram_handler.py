import os
import io
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from werkzeug.datastructures import FileStorage
import PIL.Image as img

temporary_files_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
if not os.path.exists(temporary_files_folder):
    os.makedirs(temporary_files_folder)


def create_spectrogram(audio_file: FileStorage, audio_name: str):

    audio_bytes = io.BytesIO(audio_file.read())

    y, sr = librosa.load(audio_bytes)

    spec = np.abs(librosa.cqt(y, sr=sr))
    spec = librosa.amplitude_to_db(spec, ref=np.max)

    output_folder = os.path.join(temporary_files_folder, 'outputs')
    if not os.path.exists(temporary_files_folder):
        os.makedirs(temporary_files_folder)
    image_output = os.path.join(output_folder, f'{audio_name}_spectrogram.png')

    plt.imsave(image_output, spec, cmap='gray')
    image = img.open(image_output)
    new_image = image.resize((256, 256))
    new_image.save(image_output)
