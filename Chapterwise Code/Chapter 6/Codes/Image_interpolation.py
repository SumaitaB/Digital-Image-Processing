import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.transform import rescale, resize, downscale_local_mean

# Load the image
c = io.imread('D:\\4-1\\DIP LAB\\dataset\\cameraman.jpg')

# Extract the desired region of interest
head = c[32:96, 89:153]

# Convert the image to grayscale
head_gray = np.mean(head, axis=2)

# Display the original image
plt.imshow(head_gray, cmap='gray')
plt.show()

# Rescale the image using nearest neighbor interpolation
head4n_nearest = rescale(head_gray, 2, order=0)

# Display the rescaled image using nearest neighbor interpolation
plt.imshow(head4n_nearest, cmap='gray')
plt.show()

# Rescale the image using bilinear interpolation
head4n_bilinear = rescale(head_gray, 2, order=1)

# Display the rescaled image using bilinear interpolation
plt.imshow(head4n_bilinear, cmap='gray')
plt.show()


# Rescale the image using bicubic interpolation
head4n_bicubic = rescale(head_gray, 2, order=3)

# Display the rescaled image using bilinear interpolation
plt.imshow(head4n_bicubic, cmap='gray')
plt.show()
