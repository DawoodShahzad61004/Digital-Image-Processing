import numpy as np
import argparse
import cv2 as cv
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original", image)

cropped = image[:100, 148:258]
cv.imshow("Cropped", cropped)

cv.waitKey(0)