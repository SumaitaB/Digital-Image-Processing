import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt

img1 = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.1.12.tiff')
io.imshow(img1)
io.show()
fig = plt.figure()
fig.show(io.imshow((img1>40) & (img1<80)))
io.show()
