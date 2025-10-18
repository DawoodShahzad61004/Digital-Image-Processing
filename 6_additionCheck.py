import cv2
import numpy as np

# -----------------------------------------------------------
# 1️⃣ Create a 5x5 RGB image (3 channels) with given values
# -----------------------------------------------------------
# Each pixel has 3 values (R, G, B), each ranging from 0–255

data = [
    [120, 200, 114, 0, 11],
    [140, 220, 143, 0, 81],
    [150, 210, 123, 0, 41],
    [160, 230, 223, 0, 21],
    [170, 101, 223, 0, 91]
]

# Convert it into a NumPy array and replicate it across 3 channels (RGB)
image = np.stack([np.array(data, dtype=np.uint8)] * 3, axis=-1)
print("Original Image Matrix (5x5x3):\n", image[:, :, 0], "\n")  # print only one channel for simplicity

# -----------------------------------------------------------
# 2️⃣ Add 250 to every pixel using OpenCV (saturated addition)
# -----------------------------------------------------------
opencv_added = cv2.add(image, 250)
print("After OpenCV Addition (Clipped to 255):\n", opencv_added[:, :, 0], "\n")

# -----------------------------------------------------------
# 3️⃣ Add 250 to every pixel using NumPy (wrap-around addition)
# -----------------------------------------------------------
numpy_added = image + 250
print("After NumPy Addition (Wrapped around 256):\n", numpy_added[:, :, 0], "\n")

# -----------------------------------------------------------
# 4️⃣ Display results visually (optional)
# -----------------------------------------------------------
# Uncomment the lines below if you want to see the difference
# cv2.imshow("Original Image", image)
# cv2.imshow("OpenCV Addition (Clipped)", opencv_added)
# cv2.imshow("NumPy Addition (Wrapped)", numpy_added)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
