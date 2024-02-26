import numpy as np
from scipy.fft import fftshift, fft2
from skimage import exposure
import matplotlib.pyplot as plt

a = np.zeros((256, 256))
a[77:177, 77:177] = 1

# Display the original image
plt.subplot(1, 2, 1)
plt.imshow(a, cmap='gray')
plt.title('Original Image')


af = fftshift(fft2(a))
afl = exposure.rescale_intensity(np.log(1 + np.abs(af)), out_range=(0.0, 1.0))

plt.subplot(1, 2, 2)
plt.imshow(afl, cmap='gray')
plt.title('DFT')

plt.show()






