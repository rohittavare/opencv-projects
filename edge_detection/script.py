import imutils
import cv2

img = cv2.imread("tetris.png")
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bw = cv2.threshold(grayscale, 245, 255, cv2.THRESH_BINARY_INV)[1]
cont = cv2.findContours(bw.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(cont)

im = img.copy()

print("press space...")
for c in contours:
    cv2.drawContours(im, [c], -1, (200, 0, 100), 3)
    cv2.imshow("contours", im)
    cv2.waitKey(0)
