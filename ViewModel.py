import random
from PIL import Image, ImageTk


class ViewModel:

    def __init__(self):
        self.xray = ""  # изоражение рентгена
        self.percentage_of_defeat = 0  # процент поражения лёгких

    """заглушка для кнопки загрузки"""
    def input_of_image(self, path):
        self.xray = Image.open(path)

    """заглушка для кнопки начала анализа"""
    def analysis(self):
        self.xray = Image.open("Output image.jpg")
        return self.percentage_of_defeat

    """возвращение изображения нужного размера"""
    def get_image(self,x,y):
        return ImageTk.PhotoImage(self.xray.resize((x, y), Image.ANTIALIAS))
