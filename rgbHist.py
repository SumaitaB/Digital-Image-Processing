import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read in the image
I = cv2.imread('C://Dataset//4.2.03.tiff')

# Convert the original image to HSV
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)

# Histogram equalize the V (Value) channel of Ihsv
V = cv2.equalizeHist(Ihsv[:, :, 2])

# Copy the equalized V plane into the 3rd channel of Ihsv
Ihsv[:, :, 2] = V

# Convert Ihsv back to RGB format
Iout = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)

# Display the original and modified images side by side
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(Iout, cv2.COLOR_BGR2RGB))
plt.title("Histogram Equalized Image")
plt.axis('off')

plt.show()
