import numpy as np
import skimage.io as io
import skimage.filters.rank as rk
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import skimage.restoration as re




k= io.imread('E://4-1//406 DIP Lab//DIP_LAB//Dataset//7.2.01.tiff')
cb=re.denoise_bilateral(k,win_size=7,sigma_spatial=10)

io.imshow(cb)
io.show()

