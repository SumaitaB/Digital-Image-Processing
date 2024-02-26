import numpy as np
import skimage.io as io
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
k= io.imread('E://4-1//406 DIP Lab//DIP_LAB//Dataset//7.2.01.tiff')
kf=ndi.uniform_filter(k.astype(float),3)
hb1=3*k-2*kf
hb2=1.25*k-0.25*kf
plt.subplot(121),io.imshow(hb1)
plt.subplot(122),io.imshow(hb2)

plt.show()
