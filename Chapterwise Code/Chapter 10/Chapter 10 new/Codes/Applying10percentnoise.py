import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt


c=io.imread('D://Dataset//circles.jpg').astype('bool')*1
x=np.random.random_sample(c.shape)
c[np.nonzero(x>0.95)]=0
c[np.nonzero(x<=0.95)]=1

plt.imshow(c, cmap='gray')

plt.show()
