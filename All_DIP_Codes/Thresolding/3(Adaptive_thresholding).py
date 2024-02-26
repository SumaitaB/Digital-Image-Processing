import skimage.io as io
import matplotlib.pyplot as plt
import skimage.filters as fl
import numpy as np

f = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\7.1.05.tiff')
f = f.astype(float)

plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f, cmap='gray')

r,c = f.shape
x, y = np.mgrid[0:r, 0:c].astype(float)
f1 = 255.0 - f 
plt.subplot(2,1,2)
plt.axis('off')
plt.title('Adaptive thresholded image')

plt.imshow(f1<fl.threshold_otsu(f1), cmap='gray')

plt.show()




