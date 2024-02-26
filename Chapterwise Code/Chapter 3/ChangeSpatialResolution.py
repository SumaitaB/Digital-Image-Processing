import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float, img_as_ubyte
import skimage.transform as tr


c = io.imread("D:\\dataset\\5.3.01.tiff")
io.imshow(c)
io.show()

c4 = tr.rescale(tr.rescale(c, 0.25), 4, order = 0)
io.imshow(c4)
io.show()
