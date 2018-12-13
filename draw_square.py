import cv2
import numpy as np

"""
    Function
"""


def draw_rectangle(event, x, y ,flags, param):
    pass


cv2.namedWindow(winname="drawing")
cv2.setMouseCallback("drawing", draw_rectangle)
"""
    Showing the image with OpenCV
"""

img = np.zeros((512, 512, 3))

while True:
    cv2.imshow("drawing", img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
