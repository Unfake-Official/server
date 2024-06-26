from io import BytesIO
import librosa
import librosa.display
import numpy as np
from PIL import Image


def create_spectrogram(audio: BytesIO) -> BytesIO:
    y, sr = librosa.load(audio)

    spec = np.abs(librosa.cqt(y, sr=sr))
    spec = librosa.amplitude_to_db(spec, ref=np.max)

    # converts to type uint8, which is needed for Image.fromarray
    spec = spec.astype(np.uint8)

    spec_image = Image.fromarray(spec)

    img_bytesio = BytesIO()
    spec_image.save(img_bytesio, format='PNG')
    img_bytesio.seek(0)

    return img_bytesio
