import numpy as np
import skimage.io as io
import skimage.filters.rank as rk
import scipy.ndimage as ndi
import matplotlib.pyplot as plt



k= io.imread('E://4-1//406 DIP Lab//DIP_LAB//Dataset//7.2.01.tiff')
cd=np.float32(k)
cdm=ndi.uniform_filter(cd,(3,3))
cd2f=ndi.uniform_filter(cd**2,(3,3))
cdv=cd2f-cdm**2
io.imshow(cdv)
io.show()
