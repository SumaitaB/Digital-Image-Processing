from skimage import io, color, exposure, img_as_ubyte
import numpy as np
from numpy.fft import fftshift, fft, ifft2, fft2
import matplotlib.pyplot as plt
from scipy import ndimage as ndi


cr = io.imread('D://Dataset//cameraman.png')
cr = color.rgb2gray(cr)

m=np.ones((1,7))/7
cm=ndi.correlate(cr,m)

m2=np.zeros_like(cr)
m2[1,0:7]=m
mf=fft2(m2)

bmi=ifft2(fft2(cm)/mf)
output= exposure.rescale_intensity(abs(bmi), out_range=(0,1))

d=0.02
mf=fft2(m2)
mf[np.where(abs(mf)<d)]=1
bmi = abs(ifft2(fft2(cm)/mf))
bmu=img_as_ubyte(bmi/bmi.max())
output2= exposure.rescale_intensity(bmu, out_range=(0,128))



plt.subplot(2,3,1)
plt.axis('off')
plt.title('Original image')
plt.imshow(cr,cmap='gray')

plt.subplot(2,3,3)
plt.axis('off')
plt.title('Blurred image')
plt.imshow(cm,cmap='gray')

plt.subplot(2,3,4)
plt.axis('off')
plt.title('Straight division image')
plt.imshow(output,cmap='gray')

plt.subplot(2,3,6)
plt.axis('off')
plt.title('Constrained division image')
plt.imshow(output2,cmap='gray')

plt.show()
