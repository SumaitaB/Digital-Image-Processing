import numpy as np
import skimage.io as io
import skimage.color as color
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

# Load the grayscale image
img = io.imread('C:\\Dataset\\boat.512.tiff')

# Apply Gaussian filter
gaussian_filtered = ndi.gaussian_filter(img, sigma=1)

# Apply Laplace filter
laplace_filtered = ndi.laplace(img)

# Create a figure with 1 row and 3 columns of subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot original image
axes[0].imshow(img, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

# Plot Gaussian filtered image
axes[1].imshow(gaussian_filtered, cmap='gray')
axes[1].set_title('Gaussian Filtered')
axes[1].axis('off')

# Plot Laplace filtered image
axes[2].imshow(laplace_filtered, cmap='gray')
axes[2].set_title('Laplace Filtered')
axes[2].axis('off')

# Show the plots
plt.tight_layout()
plt.show()
