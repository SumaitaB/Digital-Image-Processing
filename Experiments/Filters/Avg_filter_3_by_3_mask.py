import skimage.io as io
import numpy as np
import scipy.ndimage as ndi

img01= io.imread('U:\\4-1\\Digital Image Processing LAB\\LAB_1(12-04-2022)\\Dataset\\misc\\7.2.01.tiff')

io.imshow(img01)
io.show()

f=np.ones((3,3))/9.0

img02= ndi.convolve(img01, f, mode='constant')

io.imshow(img02)
io.show()
