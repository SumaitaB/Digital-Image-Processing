import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import skimage.util as ut
from numpy.fft import *
import skimage.exposure as ex
g=io.imread('5.3.01.tiff')
r,c=g.shape
x,y=np.mgrid[0:r,0:c].astype('float32')
p=np.sin(x/3+y/3)+1.0
gp=(2*ut.img_as_float(g)+p/2)/3
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(g,cmap='gray')
plt.subplot(1,2,2)
plt.title('Image with Periodic Noise')
plt.imshow(gp,cmap='gray')
plt.show()

#DFT of noisy image and position of spike
gf=fftshift(fft2(gp))
mg_spectrum=np.abs(gf)

temp= ex.rescale_intensity(abs(gf),out_range=(0,1))
plt.title('DFT of noisy image')
plt.imshow(np.log10(1+mg_spectrum),cmap='gray')
plt.show()


#Applying band Reject filter
#Position of spikes
gf2=ut.img_as_ubyte(temp)
gf2[512,512]=0  #center of dft
i,j=np.where(gf2==gf2.max())
print(i)
print(j)

print((i-512)**2+(j-512)**2)
z=np.sqrt((x-512)**2+(y-512)**2)
k=1 #This value can vary ... k=2,5 etc.
d=np.sqrt(5832)
br=(z<np.floor(d-k))|(z>np.ceil(d+k))
gfr=gf*br

plt.title('Filtered dft magnitude spectrum')
plt.imshow(np.log10(1+np.abs(gfr)),cmap='gray')
plt.show()

filtered_gp = np.real(ifft2(ifftshift(gfr)))
# Show the filtered image
plt.title('Filtered Image')
plt.imshow(filtered_gp, cmap='gray')
plt.show()



#Applying CrissCross Filter
gf2=np.copy(gf)
gf2[i,:]=0
gf2[:,j]=0
plt.title('Filtered dft magnitude spectrum')
plt.imshow(np.log10(1+np.abs(gf2)),cmap='gray')
plt.show()
filtered_gp = np.real(ifft2(ifftshift(gfr)))
# Show the filtered image
plt.title('Filtered Image')
plt.imshow(filtered_gp, cmap='gray')
plt.show()

