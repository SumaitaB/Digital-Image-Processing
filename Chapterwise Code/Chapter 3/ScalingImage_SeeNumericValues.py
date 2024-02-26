import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float

c = io.imread("D:\\dataset\\5.3.01.tiff")
io.imshow(c)
io.show()

cd1 = c.astype(float)
cd2 = img_as_float(c)

print(c.dtype)
print(c.min(), c.max())

print(cd1.dtype)
print(cd1.min(), cd1.max())

print(cd2.dtype)
print(cd2.min(), cd2.max())
