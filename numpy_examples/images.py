import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image


def images_processing():
    pic = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/cat_picture.jpg")
    print(pic)
    pic_arr = np.asarray(pic)
    print(pic_arr)
    print(pic_arr.shape)

