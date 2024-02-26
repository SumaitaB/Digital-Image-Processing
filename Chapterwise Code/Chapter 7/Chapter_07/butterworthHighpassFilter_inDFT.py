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

# Define the Butterworth high-pass filter
D = 15
bh = 1 - 1 / (1 + ((x ** 2 + y ** 2) / D ** 2) ** 2)

# Apply the Butterworth high-pass filter to the Fourier spectrum
cfbh = cf * bh

# Compute the inverse Fourier transform
filtered_image = np.abs(ifft2(cfbh))

# Create a figure with two subplots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2)

# Display the Fourier spectrum
axes[0].imshow(exposure.rescale_intensity(np.log(1 + np.abs(cfbh)), out_range=(0, 1)), cmap='gray')
axes[0].set_title('The DFT after Butterworth high pass filtering')

# Display the resulting image
axes[1].imshow(filtered_image, cmap='gray')
axes[1].set_title('The resulting Image')

# Remove ticks and labels from subplots
for ax in axes:
    ax.axis('off')

# Adjust the spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()
