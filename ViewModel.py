import pydicom
from PIL import Image

import back.model_manager as model_manager


def apply_ct_window(img, window):
    # window = (window width, window level)
    R = (img - window[1] + 0.5 * window[0]) / window[0]
    R[R < 0] = 0
    R[R > 1] = 1
    return R


class ViewModel:

    def __init__(self):
        self.xray = ""  # изоражение рентгена
        self.percentage_of_defeat = 0  # процент поражения лёгких
        self.model = model_manager.AiModel('back\\')

    def input_of_image(self, path):
        """заглушка для кнопки загрузки"""

        ds = pydicom.read_file(path)
        image = ds.pixel_array
        image = image.astype(float)
        image = image * ds.RescaleSlope + ds.RescaleIntercept
        image = apply_ct_window(image, [400, 50])

        image = Image.fromarray((255 * image).astype('int8'))
        image = image.convert('RGB')
        self.xray = image

    def analysis(self):
        """Возвращает результат работы нейросети(0-кот, 1-собака)"""

        return self.model.get_result(self.xray)

    def get_image(self, x, y):
        """возвращение изображения нужного размера"""

        return self.xray.resize((x, y), Image.ANTIALIAS)
