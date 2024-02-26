import numpy as np
import skimage.io as io
import scipy.ndimage as ndi

img01= io.imread('E://4-1//406 DIP Lab//DIP_LAB//Dataset//7.2.01.tiff')
io.imshow(img01)
io.show()

f=np.ones((9,9))/81

img02= ndi.convolve(img01, f, mode='constant')

io.imshow(img02)
io.show()

cf=ndi.uniform_filter(img01,25)
io.imshow(cf)
io.show()

cf=ndi.uniform_filter(img01,50)
io.imshow(cf)
io.show()
