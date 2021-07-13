import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow import keras


class AiModel:
    def __init__(self, path):
        self.model = keras.models.load_model(path + 'gosha_model')
        self.model.load_weights(path + 'model_weights')

    def get_result(self, image):
        """на вход принимает изображение из vm.xray, возвращает результат работы НС"""
        image = image.resize((256, 256), Image.ANTIALIAS)
        res = self.model.predict(tf.expand_dims(image, axis=0))

        return np.argmax(res)
