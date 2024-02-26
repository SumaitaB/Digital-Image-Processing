import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

img = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.3.01.tiff')
io.imshow(img)
io.show()

f = plt.figure()
f.show(plt.hist(img.flatten(), bins=256))

plt.show()
