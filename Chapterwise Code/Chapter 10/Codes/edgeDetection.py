import skimage.morphology as mo
import skimage.io as io
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage.color import rgb2gray


n= io.imread('D://Dataset//circles.jpg')
n_gray = rgb2gray(n) 


str1=mo.square(5)
str2=mo.disk(1)

cd=mo.dilation(n_gray,str1)-mo.erosion(n_gray,str1)


plt.subplot(1,4,1)
plt.axis('off')
plt.title('Original')
plt.imshow(n,cmap='gray')

plt.subplot(1,4,2)
plt.title('Edge detected')
plt.axis('off')
plt.imshow(cd,cmap='gray')




plt.show()


