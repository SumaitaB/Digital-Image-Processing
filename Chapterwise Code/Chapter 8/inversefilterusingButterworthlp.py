from skimage import io, color, exposure
import numpy as np
from numpy.fft import fftshift, fft, ifft2, fft2
import matplotlib.pyplot as plt



b=io.imread('D://Dataset//cameraman.png')
b = color.rgb2gray(b)
bf=fftshift(fft2(b))
r,c=b.shape
x, y = np.mgrid[-c/2:c/2, -r/2:r/2]
bworth=1/(1+(np.sqrt(2)-1)*((x**2+y**2)/15**2)**2)
bw=bf*bworth
bwa=abs(ifft2(bw))
blur = exposure.rescale_intensity(bwa, out_range=(0.0, 1.0))



blf=fftshift(fft2(blur))
blfw=blf/bworth
bla=abs(ifft2(blfw))

normalized_bla = (bla - np.min(bla)) / (np.max(bla) - np.min(bla))

blf=fftshift(fft2(blur))
d=40
bworth2=1/(1+(np.sqrt(2)-1)*((x**2+y**2)/d**2)**10)
blfb=blf/bworth*bworth2
bla=abs(ifft2(blfb))

output= exposure.rescale_intensity(bla, out_range=(0.0, 1.0))

d=0.01
bw=np.copy(bworth)
bw[np.where(bw>d)]=1
fbw=fftshift(fft2(blur))/bw
ba=abs(ifft2(fbw))
output2= exposure.rescale_intensity(ba, out_range=(0.0, 1.0))



plt.subplot(2,3,1)
plt.axis('off')
plt.title('Blurred image')
plt.imshow(blur,cmap='gray')

plt.subplot(2,3,3)
plt.axis('off')
plt.title('DeBlurred image')
plt.imshow(bla,cmap='gray')

plt.subplot(2,3,4)
plt.axis('off')
plt.title('DeBlurred image with D=40')
plt.imshow(output,cmap='gray')

plt.subplot(2,3,6)
plt.axis('off')
plt.title('DeBlurred image with D=0.01')
plt.imshow(output2,cmap='gray')


plt.show()

