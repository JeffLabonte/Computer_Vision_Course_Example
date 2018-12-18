import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Computer-Vision-with-Python/DATA/dog_backpack.png")
plt.imshow(img)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)

new_img = img_rgb.copy()
new_img = cv2.flip(new_img, 0)
plt.imshow(new_img)


pt1 = (200, 380)
pt2 = (600, 700)
cv2.rectangle(img_rgb, pt1=pt1, pt2=pt2, color=(255,0,0), thickness=10)
plt.imshow(img_rgb)

vertices = np.array([ [200, 700], [ 425, 400 ], [600, 700] ], np.int32)
vertices.shape

pts = vertices.reshape((-1, 1, 2))

cv2.polylines(img_rgb, [pts], isClosed=True, color=(0,0,255), thickness=29)

plt.imshow(img_rgb)