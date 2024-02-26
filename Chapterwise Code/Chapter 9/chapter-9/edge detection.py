import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters 

img = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.1.12.tiff')
io.imshow(img)
io.show()

#prewitt filter
edge_p = filters.prewitt(img)
io.imshow(edge_p)
io.show()

#roberts filter
edge_r = filters.roberts(img)
io.imshow(edge_r)
io.show()

#sobel filter
edge_s = filters.sobel(img)
io.imshow(edge_s)
io.show()

