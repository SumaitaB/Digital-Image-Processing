import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import skimage.util.noise as noise
import skimage.util as util

img = io.imread('5.3.01.tiff')
io.imshow(img)
io.show()

# adding salt and pepper noise
sp = noise.random_noise(img, mode='s&p', amount = 0.3)
# adding gaussian noise
mean = 0
var = 0.3
g = noise.random_noise(img, mode='gaussian', mean=mean, var=var)
# adding speckle noise
s = noise.random_noise(img, mode='speckle', mean=mean, var=var)
# adding periodic noise
r, c = img.shape
x, y = np.mgrid[0:r, 0:c].astype('float32')
p = np.sin(x / 3 + y / 3) + 1.0
gp = (2 * util.img_as_float(img) + p / 2) / 3

# Salt and pepper noise
plt.subplot(2, 2, 1)
plt.axis('off')
plt.imshow(sp, cmap='gray')
plt.title('Salt and Pepper Noise')

# Gaussian noise
plt.subplot(2, 2, 2)
plt.axis('off')
plt.imshow(g, cmap='gray')
plt.title('Gaussian Noise')

# Speckle noise
plt.subplot(2, 2, 3)
plt.axis('off')
plt.imshow(s, cmap='gray')
plt.title('Speckle Noise')

# Periodic noise
plt.subplot(2, 2, 4)
plt.axis('off')
plt.imshow(gp, cmap='gray')
plt.title('Periodic Noise')

plt.show()
