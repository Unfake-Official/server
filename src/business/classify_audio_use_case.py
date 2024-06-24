from werkzeug.datastructures import FileStorage
from src.infrastructure.spectrogram_handler import create_spectrogram
from src.infrastructure.inference_handler import inference


class ClassifyAudioUseCase:
    def classify(self, audio: FileStorage):
        self.__create_spectrogram(audio)
        #classification = inference(spectrogram)
        return 0

    def __create_spectrogram(self, audio: FileStorage) -> str:
        # filename = os.path.join(temporary_files_folder, filename)
        # audio.save(filename)
        create_spectrogram(audio)
        # return spectrogram
