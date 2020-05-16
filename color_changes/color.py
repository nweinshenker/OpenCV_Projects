import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread("watch.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("image", img)
k = cv2.waitKey(0)
if k == 27:         # Waits for the escape key                 
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('watchgray.png',img)
    cv2.destroyAllWindows()