from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
# print(ap)
ap.add_argument("-i", "--imageToWork", required=True, help="path to input image")
args = vars(ap.parse_args())
# print(args)

image = cv2.imread(args["imageToWork"])
# print(image)
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {} pixels".format(image.shape[2]))

cv2. imshow("Image", image)
cv2.waitKey(0)

cv2.imwrite("newimage.jpg", image)