import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from  skimage.morphology import binary_opening as opening

f = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\binary_img.png')
plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f,cmap='binary')

sq = np.ones((3,3))
td = opening(f,sq)
 
plt.subplot(2,1,2)
plt.axis('off')
plt.title('After opening image')
plt.imshow(td,cmap='binary')

plt.show()
