import cv2

img = cv2.imread("cat_picture.jpg")

while True:
    cv2.imshow('Cat', img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()