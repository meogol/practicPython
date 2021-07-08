from PIL import Image, ImageTk
import numpy as np

def read_data(path):
    arr = np.array

    xray = Image.open(path)
    return ImageTk.PhotoImage(xray.resize((400, 500), Image.ANTIALIAS))

