# ============================
# Interpolation (Concept)
# ============================
# Interpolation = "filling in the gaps" between known data points.
# In image processing, it means estimating new pixel values
# when resizing, rotating, or transforming an image.
#
# Example:
#   If pixel A = 100 and pixel B = 200,
#   then a pixel halfway between them could be 150.
#
# Why it's needed:
# - When enlarging an image → new pixels must be created.
# - When shrinking → multiple pixels merge into one (averaged).
#

# ========================================================
# OpenCV Interpolation Methods (Mathematical Overview)
# ========================================================
#
# 1. NEAREST NEIGHBOR (cv2.INTER_NEAREST)
#    - Algorithm:
#        Pick the color value of the closest pixel based on the smallest
#        Euclidean distance between the target coordinate (x', y') and
#        integer pixel coordinates (x, y) in the source image.
#
#    - Euclidean Distance Formula:
#        d = sqrt((x - x')^2 + (y - y')^2)
#
#    - Math:
#        I'(x', y') = I(round(x), round(y))
#        where:
#            I'(x', y') = interpolated pixel in the new image
#            (x, y)     = coordinate of the nearest source pixel
#        Note:
#            round() follows the standard rule —
#            round down if fractional part < 0.5,
#            round up if fractional part ≥ 0.5.
#
#    - Effect:
#        Fastest but produces blocky edges.
#        Ideal for masks or categorical images.
#
# ---------------------------------------------------------------------
#
# 2. BILINEAR INTERPOLATION (cv2.INTER_LINEAR)
#    - Algorithm:
#        Uses a 2×2 neighborhood of surrounding pixels.
#        Performs linear interpolation first along x, then along y.
#    - Math:
#        If (x, y) is the mapped source coordinate:
#
#          Q1 = I(x0, y0)       Q2 = I(x0 + 1, y0)
#          Q3 = I(x0, y0 + 1)   Q4 = I(x0 + 1, y0 + 1)
#
#        Then:
#          I'(x', y') = (1 - a)(1 - b)Q1 + a(1 - b)Q2 + (1 - a)bQ3 + abQ4
#            where:
#                a = x - x0
#                b = y - y0
#    - Effect:
#        Produces smooth gradients but slightly blurs edges.
#        Common choice for natural images.
#
# ---------------------------------------------------------------------
#
# 3. BICUBIC INTERPOLATION (cv2.INTER_CUBIC)
#    - Algorithm:
#        Uses a 4×4 neighborhood (16 surrounding pixels).
#        Computes result using a cubic convolution kernel (Catmull–Rom spline, a = -0.5).
#        Interpolation in 2D is separable — performed as two 1D cubic interpolations.
#
#    - 1D Cubic Kernel:
#        w(s) = {
#           (a + 2)|s|^3 - (a + 3)|s|^2 + 1,         |s| ≤ 1
#           a|s|^3 - 5a|s|^2 + 8a|s| - 4a,           1 < |s| < 2
#           0,                                        |s| ≥ 2
#        }
#        with a = -0.5 (Catmull-Rom).
#
#    - 2D Form:
#        I'(x', y') = Σ_m=-1→2 Σ_n=-1→2 I(x0 + m, y0 + n) * w(a - m) * w(b - n)
#            where:
#                a = x - x0
#                b = y - y0
#
#    - Effect:
#        Produces very smooth, visually pleasing images with sharper transitions
#        than bilinear, but slower (uses 16 samples per pixel).
#
# ---------------------------------------------------------------------

import cv2
import numpy as np

# Create a gradient image
image = np.zeros((100, 100, 3), dtype="uint8")
for i in range(0, 100, 2):
    image[:, i] = (255, 0, 0)    # blue lines
for i in range(1, 100, 2):
    image[:, i] = (0, 255, 255)  # yellow lines

# Resize the image to a larger size using different interpolation methods
nearest = cv2.resize(image, (400, 400), interpolation=cv2.INTER_NEAREST)
linear  = cv2.resize(image, (400, 400), interpolation=cv2.INTER_LINEAR)
cubic   = cv2.resize(image, (400, 400), interpolation=cv2.INTER_CUBIC)
area    = cv2.resize(image, (50, 50),   interpolation=cv2.INTER_AREA)

# Stack the images horizontally for comparison
combined = np.hstack([nearest, cubic, linear])
# np.hstack() requires all images to have the same height.

# Add text labels on each section
cv2.putText(combined, "NEAREST", (40, 40),  cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
cv2.putText(combined, "CUBIC",   (440, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
cv2.putText(combined, "LINEAR",  (840, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

# Display the results
cv2.imshow("Original", image)
cv2.imshow("Interpolation Comparison", combined)
cv2.imshow("AREA (Downscaled)", area)
cv2.waitKey(0)
cv2.destroyAllWindows()
