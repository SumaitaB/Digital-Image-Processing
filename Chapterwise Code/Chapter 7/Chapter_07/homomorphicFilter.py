import numpy as np
import matplotlib.pyplot as plt
from skimage import io, util
from scipy.fftpack import fft2, ifft2, fftshift

def homfilt(im, cutoff, order, lowgain, highgain):
    u = im.astype('uint8')
    u[np.where(u == 0)] = 1
    lg = np.log(u.astype(float))
    ft = fftshift(fft2(lg))
    rows, cols = im.shape
    rr = np.arange(-(rows // 2), (rows + 1) // 2, 1.0)
    cr = np.arange(-(cols // 2), (cols + 1) // 2, 1.0)
    y, x = np.meshgrid(cr, rr)
    b = ft * ((highgain - lowgain) * (1.0 - cutoff))
    id = np.abs(ifft2(b))
    return np.exp(id)

# Load the newborn image
n = util.img_as_float(io.imread('newborn.png'))

# Convert image to grayscale if it has multiple channels
if n.ndim == 3:
    n = util.img_as_float(io.imread('newborn.png'))[:, :, 0]

# Generate meshgrid
ar = np.arange(256)
x, y = np.meshgrid(ar, ar)

# Resize the newborn image to match the shape of the meshgrid arrays
n_resized = util.resize(n, (256, 256), mode='reflect')

# Apply modification to the resized newborn image
nx = n_resized * (0.5 + 0.4 * np.sin((1.3 * x + 0.7 * y - 50) / 16))

# Apply homomorphic filtering
xh = homfilt(nx, 10, 2, 0.5, 2)

# Display all images in one plot
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

axes[0, 0].imshow(n, cmap='gray')
axes[0, 0].set_title('Original Newborn Image')

axes[0, 1].imshow(nx, cmap='gray')
axes[0, 1].set_title('Modified Newborn Image')

axes[1, 0].imshow(x, cmap='gray', vmax=16)
axes[1, 0].set_title('Meshgrid')

axes[1, 1].imshow(xh, cmap='gray', vmax=16)
axes[1, 1].set_title('Homomorphic Filtered Image')

plt.tight_layout()
plt.show()
