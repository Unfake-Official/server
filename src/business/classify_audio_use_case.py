from werkzeug.datastructures import FileStorage
from src.infrastructure.spectrogram_handler import create_spectrogram
from src.infrastructure.inference_handler import inference


def classify_audio_use_case(audio: FileStorage):
    audio_name = audio.filename.split('.')[0]
    create_spectrogram(audio, audio_name)

    model_inference = inference(audio_name)
    return model_inference
