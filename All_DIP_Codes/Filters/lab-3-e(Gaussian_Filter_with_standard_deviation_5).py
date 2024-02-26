import skimage.data as data
import skimage.io as io
import numpy as np
import scipy.ndimage as ndi

# Gaussian Filter with standard deviation = 5
img01= data.camera()

io.imshow(img01)
io.show()

img02= ndi.gaussian_filter(img01,5,truncate=3)

io.imshow(img02)
io.show()
