"""
The CIELAB (abbreviated as Lab) color space consists of three color channels,
expressing the color of a pixel as three tuples (L, a, b),
where the L channel stands for luminosity/illumination/intensity (lightness).
The a and b channels represent the green-red and blue-yellow color components, respectively.
"""

import numpy as np
from skimage.io import imread
from skimage.color import rgb2lab, lab2rgb
import matplotlib.pylab as plt

im = plt.imread('U:\\4-1\\Digital Image Processing LAB\\DIP_LAB\DIP_LAB\\Dataset\\4.2.07.tiff')

im1 = rgb2lab(im)

im1_L=im1[:,:,0]
im1_a=im1[:,:,1]
im1_b=im1[:,:,2]

plt.subplot(1,2,1)
plt.axis('off')
plt.title('Original RGB color image')
plt.imshow(im)

plt.subplot(1,2,2)
plt.axis('off')
plt.title('L*a*b image')
plt.imshow(im1)
plt.show()


plt.subplot(1,3,1)
plt.axis('off')
plt.title('Luminosity(L) or intensity component')
plt.imshow(im1_L)

plt.subplot(1,3,2)
plt.axis('off')
plt.title('Green-Red Component(a*)')
plt.imshow(im1_a)

plt.subplot(1,3,3)
plt.axis('off')
plt.title('Blue-Yellow Component(b*)')
plt.imshow(im1_b)
plt.show()

rcon_img = im1_L + im1_a+im1_b
#plt.subplot(1,5,5)
plt.axis('off')
plt.title('Reconstructed L*a*b image')
plt.imshow(rcon_img)
plt.show()

rcon_img1 = np.dstack((im1_L,im1_a,im1_b))

#plt.subplot(1,5,5)
plt.axis('off')
plt.title('Reconstructed L*a*b image')
plt.imshow(rcon_img1)

plt.show()

original_img = lab2rgb(rcon_img1)
plt.axis('off')
plt.title('Original RGB color image')
plt.imshow(original_img)

plt.show()




