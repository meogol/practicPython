import random
from PIL import Image, ImageTk


class ViewModel:

    def __init__(self):
        self.xray = ""  # изоражение рентгена
        self.percentage_of_defeat = 0  # процент поражения лёгких

    def input_of_image(self, path):
        self.xray = Image.open(path)

    def analysis(self):
        self.xray = Image.open("Output image.jpg")
        return self.percentage_of_defeat

    def get_image(self):
        return ImageTk.PhotoImage(self.xray.resize((400, 500), Image.ANTIALIAS))
