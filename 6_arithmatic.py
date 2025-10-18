from __future__ import print_function
import numpy as np
import cv2 as cv
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original", image)

# print("max of 255: {}".format(cv.add(np.uint8([200]), np.uint8([100]))))
# print("min of 0: {}".format(cv.subtract(np.uint8([50]), np.uint8([100]))))

# print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
# print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

# print(np.uint8(200))
# print(np.uint8(100))
# print(np.uint8(50))

M = np.ones(image.shape, dtype="uint8") * 100
# added = cv.add(image, M)
added = image + M
cv.imshow("Added", added)
np.savetxt("Added_image_array.txt", added.reshape(-1, added.shape[2]), fmt="%d")

# subtracted = cv.subtract(image, M)
subtracted = image - M
cv.imshow("Subtracted", subtracted)
np.savetxt("Subtracted_image_array.txt", subtracted.reshape(-1, subtracted.shape[2]), fmt="%d")

cv.waitKey(0)


# ============================================================
# OpenCV 4.12 vs Older Versions
# ============================================================

# The book uses an older version of OpenCV (like 3.x or early 4.x).
# In those versions, OpenCV automatically *clipped* results
# of arithmetic operations to stay within the range [0, 255].

# Example (old behavior):
# -----------------------
# cv2.add(np.uint8([200]), np.uint8([100])) → [255]
# cv2.subtract(np.uint8([50]), np.uint8([100])) → [0]
#
# Explanation:
# - 200 + 100 = 300 → clipped to 255
# - 50 - 100 = -50 → clipped to 0
#
# This made sense for image pixels, because pixel values
# must always remain between 0 (black) and 255 (white).

# ============================================================
# What Happens in OpenCV 4.12.0 (Your Version)
# ============================================================

# In OpenCV 4.12.0, the internal behavior has changed.
# When you write:
#     cv2.add(np.uint8([200]), np.uint8([100]))
#
# OpenCV now automatically converts these small arrays
# into *floating-point matrices* before performing the math.

# This means:
# - Results are stored as floats (e.g., 300.0, -50.0)
# - Clipping is no longer applied
# - You get normal arithmetic results instead of clipped ones

# So your output:
# cv2.add → [[300.], [0.], [0.], [0.]]
# cv2.subtract → [[-50.], [0.], [0.], [0.]]
#
# indicates that OpenCV promoted your data to float32 matrices.

# The dots (.) mean the numbers are floats,
# and the double brackets [[...]] mean it’s a small matrix,
# not just a single number.

# ============================================================
# NumPy Still Behaves the Same
# ============================================================

# When using normal NumPy arithmetic:
#     np.uint8([200]) + np.uint8([100])
#     np.uint8([50]) - np.uint8([100])
#
# NumPy uses *wrap-around arithmetic* (mod 256), not clipping.
# - 200 + 100 = 300 → wraps to 44  (300 - 256 = 44)
# - 50 - 100 = -50 → wraps to 206  (256 - 50 = 206)
#
# So the NumPy results are still:
# [44]
# [206]

# ============================================================
# Why OpenCV Changed This
# ============================================================

# OpenCV 4.12 introduced automatic type promotion
# to handle mixed data types more consistently.
#
# It now:
# - Converts small uint8 arrays to float32 matrices automatically
# - Performs the math in floating-point precision
# - Does not clip integer overflows or underflows
#
# This is not an error — it’s just a new internal behavior
# that allows OpenCV to handle more general numeric cases.
#
# It’s only different from the book’s version because the book
# was written for an older OpenCV that clipped results.