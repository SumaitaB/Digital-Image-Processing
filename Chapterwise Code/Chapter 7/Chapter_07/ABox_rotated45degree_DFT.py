import numpy as np
from scipy.fft import fftshift, fft2
from skimage import io, exposure
import matplotlib.pyplot as plt

x, y = np.meshgrid(range(256), range(256))
b = (x + y < 329) & (x + y > 182) & (x - y > -67) & (x - y < 73)

# Display the rotated box image
plt.subplot(1, 2, 1)
plt.imshow(b, cmap='gray')
plt.title('Rotated Box')

# Compute the Fourier spectrum
bf = fftshift(fft2(b))
bfl = np.log(1 + np.abs(bf))

# Display the Fourier spectrum
plt.subplot(1, 2, 2)
plt.imshow(exposure.rescale_intensity(bfl, out_range=(0.0, 1.0)), cmap='gray')
plt.title('DFT')

# Show the figure
plt.show()
