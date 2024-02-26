import numpy as np
import skimage.io as io
from skimage import color
import matplotlib.pyplot as plt
from numpy.fft import fft2, ifft2, fftshift

    
img = io.imread('D://dataset//cameraman.png')
img = color.rgb2gray(img)
k = 0.01
bf = fftshift(fft2(img))
r,c=img.shape
x, y = np.mgrid[-c/2:c/2, -r/2:r/2]
bworth=1/(1+(np.sqrt(2)-1)*((x**2+y**2)/15**2)**2)
wl = bf*(abs(bworth)**2/(abs(bworth)**2+k)/bworth)
wla = abs(ifft2(wl))

k = 0.001
bf = fftshift(fft2(img))
r,c=img.shape
x, y = np.mgrid[-c/2:c/2, -r/2:r/2]
bworth=1/(1+(np.sqrt(2)-1)*((x**2+y**2)/15**2)**2)
wl = bf*(abs(bworth)**2/(abs(bworth)**2+k)/bworth)
wla1 = abs(ifft2(wl))

k = 0.0001
bf = fftshift(fft2(img))
r,c=img.shape
x, y = np.mgrid[-c/2:c/2, -r/2:r/2]
bworth=1/(1+(np.sqrt(2)-1)*((x**2+y**2)/15**2)**2)
wl = bf*(abs(bworth)**2/(abs(bworth)**2+k)/bworth)
wla2 = abs(ifft2(wl))



plt.subplot(2,2,1)
plt.imshow(img, cmap = 'gray')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(wla, cmap = 'gray')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(wla1, cmap = 'gray')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(wla2, cmap = 'gray')
plt.axis('off')

plt.show()
