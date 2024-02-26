import numpy as np
import skimage.io as io
import skimage.filters.rank as rk
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import skimage.restoration as re
from skimage.draw import polygon 
from skimage import util as ut
from skimage import filters as fl


m2= io.imread('E://4-1//406 DIP Lab//DIP_LAB//Dataset//5.3.01.tiff')
io.imshow(m2)
io.show()
m=m2[33:393,205:604]
r,c=m.shape

xi=np.array([60,27,14,78,130,139])
yi=np.array([14,38,127,177,160,69])
roi=np.zeros_like(m)
r,c=polygon(yi,xi)
roi[c,r]=1
g=1.5 #deviaation
mg=ut.img_as_ubyte(fl.gaussian(m,g))
mr=mg*roi+m*(1-roi)

io.imshow(mr)
io.show()


