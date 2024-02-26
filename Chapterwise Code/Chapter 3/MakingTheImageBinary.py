import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float, img_as_ubyte

c = io.imread("D:\\dataset\\5.3.01.tiff")
io.imshow(c)
io.show()

cl = c > 120
print(cl.dtype)

img_as_ubyte(cl)
print(np.uint8(cl*255))
print(np.float16(cl*1))

