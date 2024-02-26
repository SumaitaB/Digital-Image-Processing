import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters 

b = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.1.12.tiff')
p = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.3.01.tiff')
n = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.3.02.tiff')

io.imshow(b > filters.threshold_otsu(b))
io.show()
io.imshow(p > filters.threshold_otsu(p))
io.show()
io.imshow(n > filters.threshold_otsu(n))
io.show()

