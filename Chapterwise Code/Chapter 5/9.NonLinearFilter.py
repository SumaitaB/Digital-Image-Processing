import numpy as np
import skimage.io as io
import skimage.filters.rank as rk
import scipy.ndimage as ndi
import matplotlib.pyplot as plt

def rms(x):
    return np.sqrt(np.mean(x**2))


k= io.imread('E://4-1//406 DIP Lab//DIP_LAB//Dataset//7.2.01.tiff')
cmax=ndi.generic_filter(k,max,[3,3])
cmin=ndi.generic_filter(k,min,[3,3])

io.imshow(cmax)
io.show()
io.imshow(cmin)
io.show()

cmax=rk.minimum(k,np.ones((3,3)))
cmin=ndi.minimum_filter(k,size=(3,3))
io.imshow(cmax)
io.show()
io.imshow(cmin)
io.show()

cm=ndi.median_filter(k,size=(3,3))
cm2=ndi.rank_filter(k,4,size=(3,3))
io.imshow(cm)
io.show()
io.imshow(cm2)
io.show()

cr=ndi.generic_filter(k,rms,size=(3,3))
io.imshow(cr)
io.show()

