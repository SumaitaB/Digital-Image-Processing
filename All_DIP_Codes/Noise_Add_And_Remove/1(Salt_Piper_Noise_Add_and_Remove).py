import numpy as np
import scipy.ndimage as ndi
import skimage.io as io
import matplotlib.pyplot as plt
from skimage.util import random_noise

img = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\5.3.01.tiff')

plt.title('Original Image')
plt.axis('Off')
plt.imshow(img, cmap='gray')
plt.show()

img_noise1 = random_noise(img, mode='s&p',amount=0.05)
img_noise2 = random_noise(img, mode='s&p',amount=0.1)
img_noise3 = random_noise(img, mode='s&p',amount=0.15)

plt.subplot(1,3,1)
plt.title('5% noisy image')
plt.axis('Off')
plt.imshow(img_noise1, cmap='gray')


plt.subplot(1,3,2)
plt.title('10% noisy image')
plt.axis('Off')
plt.imshow(img_noise2, cmap='gray')

plt.subplot(1,3,3)
plt.title('15% noisy image')
plt.axis('Off')
plt.imshow(img_noise3, cmap='gray')

plt.show()

# Low pass filter

img_LP_filter1=ndi.uniform_filter(img_noise1,3)
img_LP_filter2=ndi.uniform_filter(img_noise2,3)
img_LP_filter3=ndi.uniform_filter(img_noise3,3)

plt.subplot(3,1,1)
plt.title('remove 5% noise using LP filter')
plt.axis('Off')
plt.imshow(img_LP_filter1, cmap='gray')


plt.subplot(3,1,2)
plt.title('remove 10% noise using LP filter')
plt.axis('Off')
plt.imshow(img_LP_filter1, cmap='gray')

plt.subplot(3,1,3)
plt.title('remove 15% noise using LP filter')
plt.axis('Off')
plt.imshow(img_LP_filter1, cmap='gray')

plt.show()

# Median Filter
img_median_filter1=ndi.median_filter(img_noise1,3)
img_median_filter2=ndi.median_filter(img_noise2,3)
img_median_filter3=ndi.median_filter(img_noise3,3)

plt.subplot(3,1,1)
plt.title('remove 5% noise using median filter')
plt.axis('Off')
plt.imshow(img_median_filter1, cmap='gray')


plt.subplot(3,1,2)
plt.title('remove 10% noise using median filter')
plt.axis('Off')
plt.imshow(img_median_filter1, cmap='gray')

plt.subplot(3,1,3)
plt.title('remove 15% noise using median filter')
plt.axis('Off')
plt.imshow(img_median_filter1, cmap='gray')

plt.show() 

# Rank Order Filter
mask = np.array([
                [0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]
                ])

img_rank_order_filter1=ndi.median_filter(img_noise1,footprint=mask)
img_rank_order_filter2=ndi.median_filter(img_noise2,footprint=mask)
img_rank_order_filter3=ndi.median_filter(img_noise3,footprint=mask)

plt.subplot(3,1,1)
plt.title('remove 5% noise using rank-order filter')
plt.axis('Off')
plt.imshow(img_rank_order_filter1, cmap='gray')


plt.subplot(3,1,2)
plt.title('remove 10% noise using rank-order filter')
plt.axis('Off')
plt.imshow(img_rank_order_filter1, cmap='gray')

plt.subplot(3,1,3)
plt.title('remove 15% noise using rank-order filter')
plt.axis('Off')
plt.imshow(img_rank_order_filter1, cmap='gray')

plt.show()


# Outlier Method
avg_mask = np.array([
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
                ])/8.0

img_filter1=ndi.convolve(img_noise1,avg_mask)
img_filter2=ndi.convolve(img_noise2,avg_mask)
img_filter3=ndi.convolve(img_noise3,avg_mask)
D = 0.5
r = ( (img_noise1-img_filter1) > D )*1.0
plt.subplot(3,1,1)
plt.title('remove 5% noise using outlier method')
plt.axis('Off')
plt.imshow(r*img_filter1 + (1-r)*img_noise1, cmap='gray')


plt.subplot(3,1,2)
plt.title('remove 10% noise using outlier method')
plt.axis('Off')
plt.imshow(r*img_filter1 + (1-r)*img_noise2, cmap='gray')

plt.subplot(3,1,3)
plt.title('remove 15% noise using outlier method')
plt.axis('Off')
plt.imshow(r*img_filter1 + (1-r)*img_noise3, cmap='gray')

plt.show()
