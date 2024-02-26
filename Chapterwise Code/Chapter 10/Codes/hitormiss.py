from skimage.morphology import binary_erosion
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

t= io.imread('D://Dataset//circles.jpg')
t_gray = rgb2gray(t) 
b1= np.array([[0,1,1,0],[1,1,1,1],[1,1,1,1],[0,1,1,0]])
b2=np.ones((6,6), dtype=bool);

b2[1:5,1:5]= 1-b1
tb1=binary_erosion(t_gray,b1);
tb2=binary_erosion(1-t_gray,b2);
result = np.where((tb1 & tb2) == 1)

print(result)

plt.subplot(1,3,1)
plt.axis('off')
plt.imshow(t,cmap='gray')

plt.subplot(1,3,2)
plt.axis('off')
plt.imshow(tb1,cmap='gray')

plt.subplot(1,3,3)
plt.axis('off')
plt.imshow(tb2,cmap='gray')

plt.show()


