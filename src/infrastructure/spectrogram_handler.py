from io import BytesIO
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as img


def create_spectrogram(audio: BytesIO) -> BytesIO:

    y, sr = librosa.load(audio, sr=None)

    spec = np.abs(librosa.cqt(y, sr=sr))
    spec = librosa.amplitude_to_db(spec, ref=np.max)

    img_bytesio = BytesIO()
    plt.imsave(img_bytesio, spec, cmap='viridis')
    img_bytesio.seek(0)

    image = img.open(img_bytesio).convert('RGB')
    image = image.resize((512, 256))

    img_bytesio_resized = BytesIO()
    image.save(img_bytesio_resized, format='png')
    img_bytesio_resized.seek(0)

    return img_bytesio_resized
