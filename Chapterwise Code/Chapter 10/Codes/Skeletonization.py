from skimage.morphology import  binary_erosion,skeletonize
import skimage.io as io
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage.color import rgb2gray


cr=np.array([[0,1,0],[1,1,1],[0,1,0]])
n= io.imread('D://Dataset//nicework.png')/255
n_gray = rgb2gray(n)

threshold = 0.5  
binary_image = n_gray > threshold

nk=skeletonize(n_gray)

plt.subplot(1,4,1)
plt.axis('off')
plt.imshow(n,cmap='gray')

plt.subplot(1,4,2)
plt.axis('off')
plt.imshow(nk,cmap='gray')



plt.show()


