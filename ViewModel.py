import PIL
from PIL import Image, ImageTk
import pydicom as dicom
import back.model_manager as model_manager

from matplotlib import pyplot as plt


class ViewModel:

    def __init__(self):
        self.xray = ""  # изоражение рентгена
        self.percentage_of_defeat = 0  # процент поражения лёгких
        self.model = model_manager.AiModel('back\\')

    def input_of_image(self, path):
        """заглушка для кнопки загрузки"""

        ds = dicom.dcmread(path)
        img = PIL.Image.fromarray(ds.pixel_array, "I;16")
        self.xray = img

    def analysis(self):
        """Возвращает результат работы нейросети(0-кот, 1-собака)"""

        return self.model.get_result(self.xray)

    def get_image(self, x, y):
        """возвращение изображения нужного размера"""

        return ImageTk.PhotoImage(self.xray.resize((x, y), Image.ANTIALIAS))

# a = ViewModel()
# a.input_of_image(
#     'C:\\Users\\meogol\\Desktop\\Облако Mail.ru\\razreshenie1\\BOROZDENKOVA_G.V\\19_01_2021_9_09_14\\IMG-0001-00001.dcm')
#
# img = PIL.Image.fromarray(a.xray, "I;16")
# plt.imshow(img)
# plt.show()
