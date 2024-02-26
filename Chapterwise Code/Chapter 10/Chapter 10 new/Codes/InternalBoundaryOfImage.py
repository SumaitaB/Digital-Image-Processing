from skimage.morphology import  binary_erosion
import skimage.io as io
import numpy as np
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

n = io.imread('D://Dataset//circles2.png')
r_gray = rgb2gray(n)
r_binary = r_gray > threshold_otsu(r_gray)

p = ~((r_binary > 10) & (r_binary < 256))


sq = np.ones((3, 3), dtype=bool)

pe = binary_erosion(p, sq)

p_int= p ^ pe


plt.subplot(1,3,1)
plt.axis('off')
plt.title('Original Image')
plt.imshow(n,cmap='gray')


plt.subplot(1,3,2)
plt.axis('off')
plt.imshow(p,cmap='gray')

plt.subplot(1,3,3)
plt.axis('off')
plt.imshow((p^pe),cmap='gray')
plt.show()



