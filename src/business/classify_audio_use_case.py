from werkzeug.datastructures import FileStorage
from src.infrastructure.spectrogram_handler import create_spectrogram
from src.infrastructure.inference_handler import inference


class ClassifyAudioUseCase:
    def classify(self, audio: FileStorage):
        audio_name = audio.filename
        if '.wav' in audio_name:
            spectrogram = self.__create_spectrogram(audio)
            classification = inference(spectrogram)
            return classification
        else:
            raise Exception('must be .wav')

    def __create_spectrogram(self, audio: FileStorage) -> str:
        spectrogram = create_spectrogram(audio)
        return spectrogram
