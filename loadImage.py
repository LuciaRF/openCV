import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cb_image = cv.imread('Resources/Photos/cat.jpg',0)

print("Image size is: ", cb_image.shape)
print("Data type of image is: ",cb_image.dtype)

plt.imshow(cb_image)
