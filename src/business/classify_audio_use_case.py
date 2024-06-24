from werkzeug.datastructures import FileStorage
from src.infrastructure.spectrogram_handler import create_spectrogram
from src.infrastructure.inference_handler import inference
import os


temporary_files_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
if not os.path.exists(temporary_files_folder):
    os.makedirs(temporary_files_folder)

class ClassifyAudioUseCase:
    def classify(self, audio: FileStorage):
        self.__create_spectrogram(audio)
        #classification = inference(spectrogram)
        return 0

    def __create_spectrogram(self, audio: FileStorage) -> str:
        # filename = os.path.join(temporary_files_folder, filename)
        # audio.save(filename)

        create_spectrogram(audio, temporary_files_folder)
        # return spectrogram
