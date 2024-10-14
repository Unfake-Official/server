from src.infrastructure.model.classifier import Classifier
import os
import numpy as np
from io import BytesIO
from keras import utils, models
import tensorflow as tf

absolute_path = os.path.abspath(os.path.dirname(__file__))
checkpoint_path = os.path.join(absolute_path, 'model', 'model.keras')

model = models.load_model(checkpoint_path)

def inference(spectrogram_bytes: BytesIO):

    class_names = ['fake', 'real']

    img_array = utils.img_to_array(spectrogram_bytes)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    return {
        'accuracy': 100 * np.max(predictions),
        'classification': class_names[np.argmax(predictions)]
    }
