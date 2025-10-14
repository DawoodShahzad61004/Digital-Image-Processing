import numpy as np
import cv2 as cv

image = cv.imread("images/download.png")

# Save full array to text file
np.savetxt("image_array.txt", image.reshape(-1, image.shape[2]), fmt="%d")