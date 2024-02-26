import skimage.data as data
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import skimage.util as ut
from skimage.draw import polygon
p = np.array([
    [100,400,34,89,20],
    [98,32,56,90,23],
    [67,87,20,55,68],
    [32,90,56,77,44],
    [87,45,90,43,20]
    ])
m2 = data.coins()
m = m2[55:60, 100:150]
r,c = m.shape
plt.imshow(m2)
plt.show()

xi = np.array([60,27,14,78,100,109])/255
yi = np.array([14,38,107,107,100,69])/255

roi = np.zeros_like(m)
r,c = polygon(yi,xi)
roi[c,r]=1

mg = ut.img_as_ubyte(ndi.gaussian_filter(m,2))
mr=mg*roi + m*(1-roi)

plt.imshow(mr)
plt.show()
