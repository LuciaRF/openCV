import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cat.jpg')

cv.imshow('img',img)

imageLine = img.copy()

cv.line(imageLine, (50,50),(100,100),(0,255,255),thickness=5,lineType=cv.LINE_AA)

plt.imshow(imageLine)

while True:
    if cv.waitKey(20) & 0xFF==ord('d'):
        break