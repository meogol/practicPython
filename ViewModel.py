from PIL import Image, ImageTk
import pydicom as dicom
import back.model_manager as model_manager


class ViewModel:

    def __init__(self):
        self.xray = ""  # изоражение рентгена
        self.percentage_of_defeat = 0  # процент поражения лёгких
        self.model = model_manager.AiModel('back\\')

    """заглушка для кнопки загрузки"""
    def input_of_image(self, path):
        ds = dicom.dcmread(path)

        self.xray = ds.pixel_array

    """Возвращает результат работы нейросети(0-кот, 1-собака)"""
    def analysis(self):
        return self.model.get_result(self.xray)

    """возвращение изображения нужного размера"""
    def get_image(self, x, y):
        return ImageTk.PhotoImage(self.xray.resize((x, y), Image.ANTIALIAS))

