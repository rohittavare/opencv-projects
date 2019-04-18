import numpy as np
import cv2

face = cv2.CascadeClassifier('/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

img = cv2.imread("team.jpg")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face.detectMultiScale(grayscale, 1.3, 5)
for f in faces:
    cv2.rectangle(img, (f[0], f[1]), (f[0] + f[2], f[1] + f[3]), (200, 0, 200), 3)

cv2.imshow("faces", img)
cv2.waitKey(0)
