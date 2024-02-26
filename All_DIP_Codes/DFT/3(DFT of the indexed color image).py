import numpy as np
import skimage.data as data
import skimage.io as io
import skimage.exposure as ex
import matplotlib.pyplot as plt

c = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\5.3.01.tiff')


cf = np.fft.fft2(c)
cfs = np.fft.fftshift(cf)
cfsl = np.log(1+np.abs(cfs))

plt.subplot(1,2,1)
plt.axis('off')
plt.title('Indexed color image')
plt.imshow(c, cmap='gray')

plt.subplot(1,2,2)
plt.axis('off')
plt.title('DFT of the indexed color image')
plt.imshow(ex.rescale_intensity(cfsl,out_range=(0.0,1.0)))

plt.show()

