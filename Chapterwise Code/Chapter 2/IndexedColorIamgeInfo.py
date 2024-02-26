import numpy as np
import skimage.io as io

b=io.imread('D://Dataset//4.1.02.tiff')
#io.imshow(b)
#io.show()

print (b.shape)

# to obtain values at a pixel

print(b[108,60,:])

np.set_printoptions(precision = 4)

print(b[108,60,:].astype(float)/255.0)
