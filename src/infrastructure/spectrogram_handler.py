import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

def create_spectrogram(audio_file: str):
    y, sr = librosa.load(audio_file)

    spec = np.abs(librosa.cqt(y, sr = sr))
    spec = librosa.amplitude_to_db(spec, ref = np.max)

    librosa.display.specshow(spec, y_axis = 'CQT', fmax = 8000, x_axis = 'Time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram')
    plt.show()

    # plt.imsave(output_image_file, C, cmap='gray')
    # image = img.open(output_image_file)
    # new_image = image.resize((256, 256))
    # new_image.save(output_image_file)
