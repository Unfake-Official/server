from io import BytesIO
from werkzeug.datastructures import FileStorage
from src.infrastructure.spectrogram_handler import create_spectrogram
from src.infrastructure.keras_inference_handler import inference


def classify_audio_use_case(audio: FileStorage):
    audio_bytes = BytesIO(audio.read())
    spectrogram_bytes = create_spectrogram(audio_bytes)

    model_inference = inference(spectrogram_bytes)

    audio_bytes.close()
    spectrogram_bytes.close()

    return model_inference
