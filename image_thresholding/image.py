import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Access all the different cv threshold
'''
cv2.THRESH_BINARY
cv2.THRESH_BINARY_INV
cv2.THRESH_TRUNC
cv2.THRESH_TOZERO
cv2.THRESH_TOZERO_INV
'''

def image_thres():
    # Opens the image
    img = cv.imread("mona_lisa.jpeg", cv.IMREAD_GRAYSCALE)

    # Get the thresholding values
    ret, threshold1 = cv.threshold(img, 120, 250, cv.THRESH_BINARY)
    ret, threshold2 = cv.threshold(img, 120, 250, cv.THRESH_BINARY_INV)
    ret, threshold3 = cv.threshold(img, 120, 250, cv.THRESH_TRUNC)
    ret, threshold4 = cv.threshold(img, 120, 250, cv.THRESH_TOZERO)
    ret, threshold5 = cv.threshold(img, 120, 250, cv.THRESH_TOZERO_INV)

    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, threshold1, threshold2, threshold3, threshold4, threshold5]

    for i in range(0, 6):
        plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()

if __name__ == '__main__':
    image_thres()