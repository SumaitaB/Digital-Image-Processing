
from skimage.morphology import binary_dilation
import skimage.io as io
import numpy as np
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

r = io.imread('D://Dataset//circles.jpg')
r_gray = rgb2gray(r)
r_binary = r_gray > threshold_otsu(r_gray)


sq = np.ones((3, 3), dtype=bool)

td = binary_dilation(r_binary, sq)


plt.subplot(1,3,1)
plt.axis('off')
plt.title('Original Image')
plt.imshow(r,cmap='gray')

plt.subplot(1,3,2)
plt.axis('off')
plt.title('Dilated Image')
plt.imshow(td,cmap='gray')


plt.show()



