import numpy as np
import skimage.io as io
import scipy.ndimage as ndi

img01= io.imread('E://4-1//406 DIP Lab//DIP_LAB//Dataset//7.2.01.tiff')
io.imshow(img01)
io.show()

u=np.array([[-2,-2,-2],[-2,25,-2],[-2,-2,-2]])/9.0
ku=ndi.convolve(img01.astype(float),u)
io.imshow(ku/255,vmax=1.0,vmin=0.0)
io.show()
