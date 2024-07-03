import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

imgpath = "/Users/Emile/Code/Neural-Network-v1-from-Scratch/images.jpg"

img = cv.imread(imgpath)
cv.imshow("image", img)

cv.waitKey(0)

cv.destroyAllWindows()