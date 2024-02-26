import numpy as np
from scipy.fft import fftshift, fft2
from skimage import io, exposure
import matplotlib.pyplot as plt

ar = np.arange(-128, 128)
x, y = np.meshgrid(ar, ar)
z = np.sqrt(x ** 2 + y ** 2)
c = (z < 15) * 1

# Compute the Fourier spectrum
cf = fftshift(fft2(c))
cfl = np.log(1 + np.abs(cf))

# Create a figure and two subplots
fig, axes = plt.subplots(1, 2)

# Display the small circle image in the left subplot
axes[0].imshow(c, cmap='gray')
axes[0].set_title('Small Circle')

# Display the Fourier spectrum in the right subplot
axes[1].imshow(exposure.rescale_intensity(cfl, out_range=(0.0, 1.0)), cmap='gray')
axes[1].set_title('DFT')

# Show the figure
plt.show()
