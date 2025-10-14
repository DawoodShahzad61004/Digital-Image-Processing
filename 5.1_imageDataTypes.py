# ============================
# Image Data Types in OpenCV
# ============================

# 1. uint8 (most common)
# - Range: 0–255
# - Standard for images (JPG, PNG, BMP)
# - Each channel = 1 byte, memory efficient
# - Example: canvas = np.zeros((300, 300, 3), dtype="uint8")
#   -> 300x300 pixels, 3 channels (BGR), values from 0–255
# - Used for storage & display (what monitors expect)

# 2. int32
# - Range: ~ -2.1B to +2.1B
# - Overkill for color pixels, since display still expects 0–255
# - OpenCV will usually clip or wrap values back to uint8 when displaying
# - Rarely used except for heavy math (e.g., convolution intermediate results)

# 3. float32 / float64
# - Allow fractional intensity values (e.g., 0.5, 0.25, 0.75)
# - Commonly normalized to range 0.0–1.0 in OpenCV/ML pipelines
# - Can also represent HDR or scientific imaging values >1.0
# - Example: 
#     canvas = np.zeros((300, 300, 3), dtype="float32")
#     canvas[0,0] = [0.5, 0.25, 0.75]   # 50% red, 25% green, 75% blue
# - Advantages:
#   * Higher precision
#   * Avoids rounding errors in processing
#   * Enables HDR, medical/scientific imaging

# Note: if you try to display canvas_float with cv2.imshow(),
# OpenCV will expect values between 0.0 and 1.0 and render them correctly.

# ============================
# Visualizing uint8 vs float32
# ============================

import numpy as np
import cv2

# Create two canvases: one uint8, one float32
canvas_uint8 = np.zeros((200, 200, 3), dtype="uint8")
canvas_float = np.zeros((200, 200, 3), dtype="float32")

# Assign a pixel intensity
# For uint8 → anything <1 becomes 0
canvas_uint8[:] = [0.5, 0.25, 0.75]    # will be clipped to [0,0,0]

# For float32 → fractional values are preserved
canvas_float[:] = [0.5, 0.25, 0.75]    # OpenCV treats this as [B,G,R] in 0–1 range

# Convert float image to displayable format
# (cv2.imshow can handle float32 directly if values are between 0 and 1)
# scale back to 0–255 for clearer comparison
canvas_float_disp = (canvas_float * 255).astype("uint8")
# canvas_float => canvas_float_disp = [0.5, 0.25, 0.75] * 255 = [127.5, 63.75, 191.25] => [128, 64, 191]

# Note: 
# If your float image is normalized (0–1), you don’t need to multiply by 255 just for imshow — OpenCV will display it correctly.
# But for saving, exporting, or when values exceed 1.0, scaling + conversion is safer.

# Show both images side by side
cv2.imshow("uint8 (truncated to black)", canvas_uint8)
cv2.imshow("float32 (shows dark purple)", canvas_float_disp)

cv2.waitKey(0)
cv2.destroyAllWindows()
