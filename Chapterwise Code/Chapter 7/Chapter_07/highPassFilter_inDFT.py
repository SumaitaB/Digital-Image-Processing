import numpy as np
from scipy.fft import fftshift, fft2, ifft2
from skimage import io, color
import matplotlib.pyplot as plt

# Read the Cameraman image
cm = color.rgb2gray(io.imread('cameraman.png'))

# Compute the Fourier spectrum
cf = fftshift(fft2(cm))

# Create a meshgrid
x, y = np.meshgrid(np.arange(-128, 128), np.arange(-128, 128))
z = np.sqrt(x ** 2 + y ** 2)

# Create the high pass filter
c = z > 15

# Apply the high pass filter to the Fourier spectrum
cfh = cf * c

# Compute the inverse Fourier transform
cfhi = ifft2(cfh)

# Create a figure with two subplots (1 row, 2 columns)
fig, axes = plt.subplots(1, 2)

# Display the magnitude spectrum after high pass filtering
axes[0].imshow(np.log(1 + np.abs(cfh)), cmap='gray')
axes[0].set_title('The DFT after high pass filtering')

# Display the resulting image after inverse Fourier transform
axes[1].imshow(np.abs(cfhi), cmap='gray')
axes[1].set_title('The resulting image')

# Remove ticks and labels from subplots
axes[0].axis('off')
axes[1].axis('off')

# Adjust the spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()
