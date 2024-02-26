import numpy as np
import skimage.io as io
import scipy.ndimage as ndi

img01= io.imread('E://4-1//406 DIP Lab//DIP_LAB//Dataset//7.2.01.tiff')
io.imshow(img01)
io.show()

f=np.array([[1,-2,1],[-2,4,-2],[1,-2,1]])

img02= ndi.convolve(np.float32(img01), f, mode='constant')
maximg=img01.max()
minimg=img01.min()
cf2f=(img02-minimg)/(maximg-minimg)
io.imshow(cf2f)
io.show()


io.imshow(img02/60,vmax=1.0,vmin=0.0)
io.show()
