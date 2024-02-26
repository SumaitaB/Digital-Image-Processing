import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import scipy.ndimage as ndi

# Load the image
c = io.imread('D:\\4-1\\DIP LAB\\dataset\\cameraman.jpg')

# Extract the desired region of interest
head = c[32:96, 89:153]

# Convert the image to grayscale
head_gray = np.mean(head, axis=2)

#Perform nearest neighbor interpolation enlargement
r, c = head_gray.shape
hz = np.repeat(np.repeat(head_gray, 2, axis=0), 2, axis=1)
enlarged_nearest_neighbor = ndi.convolve(hz, np.array([[1, 1], [1, 1]]) / 4.0, mode='constant')

# Perform zero interleaving enlargement
nn = np.zeros((2 * r, 2 * c)).astype('uint8')
nn[::2, ::2] = head_gray
enlarged_zero_interleaving = ndi.convolve(nn, np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), mode='constant')

# Perform bilinear interpolation enlargement
bi = np.zeros((2 * r, 2 * c)).astype('uint8')
bi[::2, ::2] = head_gray
enlarged_bilinear = ndi.convolve(bi, np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 4.0, mode='constant')

# Perform bicubic interpolation enlargement
bc = np.zeros((2 * r, 2 * c)).astype('uint8')
bc[::2, ::2] = head_gray
enlarged_bicubic = ndi.convolve(bc, np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6],
                                               [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]]) / 64.0, mode='constant')

# Display the enlarged images
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0, 0].imshow(enlarged_zero_interleaving, cmap='gray')
axes[0, 0].set_title('Zero Interleaving')
axes[0, 1].imshow(enlarged_nearest_neighbor, cmap='gray')
axes[0, 1].set_title('Nearest Neighbor')
axes[1, 0].imshow(enlarged_bilinear, cmap='gray')
axes[1, 0].set_title('Bilinear')
axes[1, 1].imshow(enlarged_bicubic, cmap='gray')
axes[1, 1].set_title('Bicubic')

plt.tight_layout()
plt.show()
