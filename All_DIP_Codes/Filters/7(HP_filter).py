import skimage.io as io
import skimage.filters as fl
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
f = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6\\Dataset\\misc\\7.1.05.tiff')
mask1 = np.array([
                [0, 1, 0],
                [1, -4, 1],
                [0, 1, 0]
                ])


mask2 = np.array([
                [1, 1, 1],
                [1, -8, 1],
                [1, 1, 1]
                ])
mask3 = np.array([
                [-2, 1, -2],
                [1, 4, 1],
                [-2, 1, -2]
                ])
plt.subplot(5,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f,cmap='gray')

plt.subplot(5,1,2)
plt.axis('off')
plt.title('Filtered image with HP filter-1')
plt.imshow(ndi.convolve(f,mask1),cmap='gray')

plt.subplot(5,1,3)
plt.axis('off')
plt.title('Filtered image with HP filter-2')
plt.imshow(ndi.convolve(f,mask2),cmap='gray')

plt.subplot(5,1,4)
plt.axis('off')
plt.title('Filtered image with HP filter-3')
plt.imshow(ndi.convolve(f,mask3),cmap='gray')

f1 = f.astype(float)
f1=fl.laplace(f)
plt.subplot(5,1,5)
plt.axis('off')
plt.title('Filtered image with Laplace filter')
plt.imshow(abs(f1),cmap='gray')

plt.show()




