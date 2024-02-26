import numpy as np
import scipy.ndimage as ndi
import skimage.io as io
import matplotlib.pyplot as plt
from skimage.util import random_noise
from scipy.signal import wiener
from numpy.fft import ifft2,fft2,fftshift
import skimage.exposure as ex
import skimage.util as ut

img = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\5.3.01.tiff')

plt.title('Original Image')
plt.axis('Off')
plt.imshow(img, cmap='gray')
plt.show()

r,c = img.shape

x,y = np.meshgrid(r,c)
p = np.sin(x/3 + y/3) + 1.0
img_noise = (2*img + p/2)/3

#img_noise1 = random_noise(img, mode='speckle')
#img_noise2 = random_noise(img, mode='s&p',amount=0.1)
#img_noise3 = random_noise(img, mode='s&p',amount=0.15)

#plt.subplot(1,3,1)
plt.title('periodic noisy image')
plt.axis('Off')
plt.imshow(img_noise, cmap='gray')


#plt.subplot(1,3,2)
#plt.title('10% noisy image')
#plt.axis('Off')
#plt.imshow(img_noise2, cmap='gray')

#plt.subplot(1,3,3)
#plt.title('15% noisy image')
#plt.axis('Off')
#plt.imshow(img_noise3, cmap='gray')

plt.show()

# Band reject filter

imgf = fftshift(fft2(img_noise))
temp = ex.rescale_intensity(abs(imgf),out_range=(0.0,1.0))
imgf2 = ut.img_as_ubyte(temp)
plt.title('DFT')
plt.axis('Off')
plt.imshow(imgf2)
plt.show()
#imgf2[200,200]=0
i,j = np.where(imgf2==imgf2.max())
print(i,j)
z = np.sqrt((i-200)**2 +(y-200)**2)
k = 1
d = np.sqrt(512.0)
br=(z<np.floor(d-k)) | (z>np.ceil(d+k))
img_dft=imgf*br

#img_LP_filter2=ndi.uniform_filter(img_noise2,3)
#img_LP_filter3=ndi.uniform_filter(img_noise3,3)

#plt.subplot(3,1,1)


imgi = fftshift(ifft2(img_dft))
temp = ex.rescale_intensity(abs(imgi),out_range=(0,1))

#plt.subplot(3,1,2)
plt.title('inverse')
plt.axis('Off')
plt.imshow(temp, cmap='gray')

#plt.subplot(3,1,3)
#plt.title('remove 15% noise using LP filter')
#plt.axis('Off')
#plt.imshow(img_LP_filter1, cmap='gray')

plt.show()

