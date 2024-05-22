from werkzeug.datastructures import FileStorage
from src.infrastructure.spectrogram_handler import create_spectrogram
from src.infrastructure.inference_handler import inference


class ClassifyAudioUseCase:
    def classify(self, audio):
        spectrogram = self.__create_spectrogram(audio)
        #classification = inference(spectrogram)
        return classification

    def __create_spectrogram(self, audio: FileStorage) -> str:
        spectrogram = create_spectrogram(audio)
        return spectrogram
