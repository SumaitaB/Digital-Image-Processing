import numpy as np
from scipy.fft import fftshift, fft2, ifft2
from skimage import io, color, exposure
import matplotlib.pyplot as plt

# Read the Cameraman image
cm = color.rgb2gray(io.imread('cameraman.png'))

# Compute the Fourier spectrum
cf = fftshift(fft2(cm))

# Create a meshgrid
ar = np.arange(-128, 128)
x, y = np.meshgrid(ar, ar)

# Define the Gaussian filter
sigma = 10
g = np.exp(-(x ** 2 + y ** 2) / sigma ** 2)
h1 = 1 - g / np.max(g)

# Apply the Gaussian filter to the Fourier spectrum
ch1 = cf * h1

# Compute the inverse Fourier transform
filtered_image = np.abs(ifft2(ch1))

# Create a figure with two subplots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2)

# Display the Fourier spectrum
axes[0].imshow(exposure.rescale_intensity(np.log(1 + np.abs(ch1)), out_range=(0, 1)), cmap='gray')
axes[0].set_title('The DFT after applying gaussian high pass filtering')

# Display the resulting image after Gaussian filtering
axes[1].imshow(filtered_image, cmap='gray')
axes[1].set_title('Resulting Image')

# Remove ticks and labels from subplots
for ax in axes:
    ax.axis('off')

# Adjust the spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()
