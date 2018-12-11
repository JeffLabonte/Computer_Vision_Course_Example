import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image


def images_processing():
    pic = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/cat_picture.jpg")
    print(pic)
    pic_arr = np.asarray(pic)
    print(pic_arr)
    print(pic_arr.shape)

    plt.imshow(pic_arr)

    pic_red = pic_arr.copy()

    # R G B
    pic_red = pic_red[:, :, 1]

