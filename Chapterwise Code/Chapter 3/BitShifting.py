import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float, img_as_ubyte

c = io.imread("D:\\Dataset\\5.3.01.tiff")
io.imshow(c)
io.show()

n = np.uint8(175)
for i in range(8):
    print (bin(n>>i))
