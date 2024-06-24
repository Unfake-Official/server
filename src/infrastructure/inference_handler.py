from src.infrastructure.model.classifier import Classifier
import numpy as np
import os
import random
# import tensorflow as tf

absolute_path = os.path.abspath(os.path.dirname(__file__))
# checkpoint_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'model', 'checkpoint')

# model = Classifier()
# model = tf.keras.models.load_model(checkpoint_path)

def inference(audio_name: str):

    path = os.path.join(absolute_path, 'uploads', audio_name)
    size = (256, 256)

    class_names = ['fake', 'other', 'real']

    # img = tf.keras.utils.load_img(path, grayscale = True, target_size = size)
    # img_array = tf.keras.utils.img_to_array(img)
    # img_array = tf.expand_dims(img_array, 0)

    # predictions = model.predict(img_array)
    # score = tf.nn.softmax(predictions[0])

    score = random.uniform(0, 1)

    return (class_names[np.argmax(score)], 100 * np.max(score))
