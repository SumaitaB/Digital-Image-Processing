import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
import skimage.util.noise as noise
import skimage.util as util
import scipy.ndimage as ndi

img = io.imread('5.3.01.tiff')
io.imshow(img)
io.show()

# adding salt and pepper noise
sp = noise.random_noise(img, mode='s&p')
io.imshow(sp)
io.show()

# apply 3*3 averaging filter
img3 = ndi.uniform_filter(sp,3)
io.imshow(img3,cmap='gray')
io.show()

# apply 7*7 averaging filter
img7 = ndi.uniform_filter(sp,7)
io.imshow(img7,cmap='gray')
io.show()

# apply median filtering
img_med = ndi.median_filter(sp,3)
io.imshow(img_med,cmap='gray')
io.show()

# apply rank order filtering
cross = np.array([[0,1,0],[1,1,1],[0,1,0]])
img_rank = ndi.median_filter(sp, footprint=cross)
io.imshow(img_rank,cmap='gray')
io.show()

# apply outlier method filtering
av = np.array([[1,1,1],[1,0,1],[1,1,1]])/8.0
spa = ndi.convolve(sp,av)
D = 0.3             # D is the threshold value to detect outliers
r = (abs(sp-spa)>D)*1.0
img_out = r*spa+(1-r)*sp
io.imshow(img_out,cmap='gray')
io.show()
