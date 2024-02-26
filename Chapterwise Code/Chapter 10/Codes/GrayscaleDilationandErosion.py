import skimage.morphology as mo
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

n= io.imread('D://Dataset//circles.jpg')
n_gray = rgb2gray(n) 


str=mo.square(5)
cd=mo.dilation(n_gray,str)
ce=mo.erosion(n_gray,str)

plt.subplot(1,4,1)
plt.axis('off')
plt.title('Original')
plt.imshow(n,cmap='gray')

plt.subplot(1,4,2)
plt.title('Dilation')
plt.axis('off')
plt.imshow(cd,cmap='gray')


plt.subplot(1,4,3)
plt.title('Erosion')
plt.axis('off')
plt.imshow(ce,cmap='gray')

plt.show()


