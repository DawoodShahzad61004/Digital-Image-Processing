import numpy as np
import cv2 as cv

canvas = np.zeros((300, 300, 3), dtype="uint8")

lineColorGreen = (0, 255, 0)
cv.line(canvas, (0, 0), (300, 300), lineColorGreen)
cv.imshow("Canvas", canvas)
cv.waitKey(0)

lineColorBlue = (255, 0, 0)
cv.line(canvas, (0, 300), (300, 0), lineColorBlue, 3)
cv.imshow("Canvas", canvas)
cv.waitKey(0)

cv.rectangle(canvas, (10, 10), (60, 60), lineColorGreen)
cv.imshow("Canvas", canvas)
cv.waitKey(0)

cv.rectangle(canvas, (50, 200), (200, 225), lineColorBlue, 5)
cv.imshow("Canvas", canvas)
cv.waitKey(0)

cv.rectangle(canvas, (200, 50), (225, 125), lineColorBlue, -1)
cv.imshow("Canvas", canvas)
cv.waitKey(0)

canvas2 = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canvas2.shape[1] // 2, canvas2.shape[0] // 2)

white = (255, 255, 255)
for r in range(0, 175, 25):
    cv.circle(canvas2, (centerX, centerY), r, white)

cv.imshow("Canvas2", canvas2)
cv.waitKey(0)

for i in range(0, 25):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    pt = np.random.randint(0, high = 300, size = (2,)) # returned an array/list of 2 integers
    cv.circle(canvas2, tuple(pt), radius, color, -1) # pt must be a tuple
    
print("pt={}, radius={}, color={}".format(pt, radius, color))
print(tuple(pt))
cv.imshow("Canvas2", canvas2)
cv.waitKey(0)