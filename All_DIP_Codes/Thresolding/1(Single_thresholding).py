import skimage.io as io
import matplotlib.pyplot as plt
import skimage.filters as fl

f = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\7.1.05.tiff')


plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f, cmap='gray')

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Single thresholded image')
plt.imshow(f<fl.threshold_otsu(f), cmap='gray')

plt.show()




