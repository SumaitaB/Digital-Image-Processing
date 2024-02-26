from skimage.morphology import  binary_erosion
import skimage.io as io
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage.color import rgb2gray


n= io.imread('D://Dataset//nicework.png')/255
n_gray = rgb2gray(n) 
sq = np.ones((3, 3), dtype=bool)
nb =n_gray -binary_erosion(n_gray,sq)
nb1=nb[0:120,0:80]
nf=ndimage.binary_fill_holes(nb1,sq)
nb[0:120,0:80]=nf

plt.subplot(1,4,1)
plt.axis('off')
plt.imshow(n,cmap='gray')

plt.subplot(1,4,2)
plt.axis('off')
plt.imshow(nf,cmap='gray')


plt.subplot(1,4,3)
plt.axis('off')
plt.imshow(nb,cmap='gray')

plt.show()


