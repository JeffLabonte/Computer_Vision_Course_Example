import cv2
import numpy as np

"""
    Variables
"""
window_name = "drawing"
drawing = False  # Becomes True once mouse is pressed down
ix, iy = -1, -1

"""
    Function
"""


def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True,
        ix,iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, (ix,iy), (x,y), (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x,y), (0, 255, 0), -1)


cv2.namedWindow(winname=window_name)
cv2.setMouseCallback(window_name, draw_rectangle)

"""
    Showing the image with OpenCV
"""

img = np.zeros((1024, 1024, 3))

while True:
    cv2.imshow(window_name, img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
