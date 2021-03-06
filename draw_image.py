import cv2
import numpy as np

"""
    Function
"""


def draw_circle(event, x, y ,flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img=img, center=(x, y), radius=100, color=(0, 255, 0), thickness=-1)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img=img, center=(x, y), radius=100, color=(255, 0, 0), thickness=-1)


cv2.namedWindow(winname="drawing")
cv2.setMouseCallback("drawing", draw_circle)
"""
    Showing the image with OpenCV
"""

img = np.zeros((512, 512, 3))

while True:
    cv2.imshow("drawing", img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()