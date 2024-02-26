import numpy as np
from scipy.fft import fftshift, fft2, ifft2
from skimage import io, exposure, color
import matplotlib.pyplot as plt

# Read the Cameraman image and convert to grayscale
cm = color.rgb2gray(io.imread('cameraman.png'))

# Compute the Fourier spectrum
cf = fftshift(fft2(cm))
cfl = np.log(1 + np.abs(cf))

# Create the ideal low pass filter
d = 15
ar = range(-128, 128)
x, y = np.meshgrid(ar, ar)
c = (x ** 2 + y ** 2 < d ** 2) * 1

# Apply the ideal low pass filter to the Fourier spectrum
cfl2 = cf * c

# Compute the inverse Fourier transform
filtered_image = np.abs(ifft2(cfl2))

# Create a figure with two subplots (2 rows, 2 columns)
plt.subplot(2, 2, 1)
plt.imshow(cm, cmap='gray')
plt.title('Cameraman Image')

plt.subplot(2, 2, 2)
plt.imshow(exposure.rescale_intensity(cfl, out_range=(0.0, 1.0)), cmap='gray')
plt.title('Fourier Spectrum')

plt.subplot(2, 2, 3)
plt.imshow(c, cmap='gray')
plt.title('Ideal Low Pass Filter')

plt.subplot(2, 2, 4)
plt.imshow(exposure.rescale_intensity(filtered_image, out_range=(0.0, 1.0)), cmap='gray')
plt.title('Inverse Fourier Transform')

# Adjust the spacing between subplots
plt.tight_layout()

# Show the figure
plt.show()
