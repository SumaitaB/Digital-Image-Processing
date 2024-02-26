import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex

f = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\7.1.05.tiff')


plt.subplot(2,1,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(f, cmap='gray')

plt.subplot(2,1,2)
plt.axis('off')
plt.title('Double thresholded image')
plt.imshow((f>40) & (f<80), cmap='gray')

plt.show()




