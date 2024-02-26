import matplotlib.pyplot as plt
from skimage.color import rgb2hsv
import numpy as np


img = plt.imread('U:\\4-1\\Digital Image Processing LAB\\DIP_LAB\DIP_LAB\\Dataset\\4.2.07.tiff')
img_hsv = rgb2hsv(img)
h = img_hsv[:,:,0]
s = img_hsv[:,:,1]
v = img_hsv[:,:,2]

plt.subplot(1,5,1)
plt.axis('off')
plt.title('RGB image')
plt.imshow(img)

plt.subplot(1,5,2)
plt.axis('off')
plt.title('Hue')
plt.imshow(h,cmap='gray')

plt.subplot(1,5,3)
plt.axis('off')
plt.title('Saturation')
plt.imshow(s,cmap='gray')

plt.subplot(1,5,4)
plt.axis('off')
plt.title('Value')
plt.imshow(v,cmap='gray')

rcon_img = np.dstack((h,s,v))

plt.subplot(1,5,5)
plt.axis('off')
plt.title('Reconstructed color image')
plt.imshow(rcon_img)


plt.show()

