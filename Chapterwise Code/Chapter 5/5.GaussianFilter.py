import numpy as np
import skimage.io as io
import scipy.ndimage as ndi

img01= io.imread('E://4-1//406 DIP Lab//DIP_LAB//Dataset//7.2.01.tiff')
io.imshow(img01)
io.show()


img02= ndi.gaussian_filter(img01,0.5,truncate=4.5)
io.imshow(img02)
io.show()

img03= ndi.gaussian_filter(img01,2,truncate=1)
io.imshow(img03)
io.show()

img04= ndi.gaussian_filter(img01,1,truncate=5)
io.imshow(img04)
io.show()

img05= ndi.gaussian_filter(img01,5,truncate=1)
io.imshow(img05)
io.show()

