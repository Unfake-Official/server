from src.infrastructure.model.classifier import Classifier
import os
import numpy as np
from io import BytesIO
from keras import Sequential, utils, layers
import tensorflow as tf

absolute_path = os.path.abspath(os.path.dirname(__file__))
checkpoint_path = os.path.join(absolute_path, 'model', 'checkpoint')

model = Classifier()
model = Sequential([layers.TFSMLayer(checkpoint_path, call_endpoint='serving_default')])

def inference(spectrogram_bytes: BytesIO):
    size = (256, 256)

    class_names = ['fake', 'real']

    img = utils.load_img(spectrogram_bytes, target_size = size)
    img_array = utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    img_array = tf.reshape(img_array, [-1, 256, 256, 1])

    predictions = model.predict(img_array)

    score = tf.nn.softmax(predictions['output_0'][0])
    return {
        'accuracy': 100 * np.max(score),
        'classification': class_names[np.argmax(score)]
    }
