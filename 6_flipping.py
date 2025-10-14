import numpy as np
import argparse
import cv2 as cv
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original", image)

flipped = cv.flip(image, 1)
cv.imshow("Flipped Horizontally", flipped)

flipped = cv.flip(image, 0)
cv.imshow("Flipped Vertically", flipped)

flipped = cv.flip(image, -1)
cv.imshow("Flipped Horizontally & Vertically", flipped)

flipped = cv.transpose(image)
cv.imshow("Flipped Along Main Diagonal", flipped)

flipped = cv.transpose(image)
flipped = cv.flip(flipped, 1)  # or use 0 for a different diagonal
cv.imshow("Flipped Along Anti-Diagonal", flipped)

(h, w) = image.shape[:2]
M = cv.getRotationMatrix2D((w//2, h//2), 45, 1.0)
rotated = cv.warpAffine(image, M, (w, h))
flipped = cv.flip(rotated, 1)
cv.imshow("Flipped Across 45-degree Axis", flipped)

cv.waitKey(0)