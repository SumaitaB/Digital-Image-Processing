import numpy as np
from skimage.morphology import binary_dilation as bwdilate
import skimage.data as data
import skimage.exposure as ex
import matplotlib.pyplot as plt

c = plt.imread('D:\\Dataset\\morph_text.png')
sel = np.ones((3,3))
c_01 = bwdilate(c,sel)


plt.subplot(1,2,1)
plt.axis('off')
plt.title('Binary image')
plt.imshow(c, cmap='gray')

plt.subplot(1,2,2)
plt.axis('off')
plt.title('Dilation (Once) of the binary image')
plt.imshow(ex.rescale_intensity(c_01,out_range=(0.0,1.0)),cmap='gray')

plt.show()

