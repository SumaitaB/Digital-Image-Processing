import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt

b = io.imread('D:\\4-1\\DIP LAB\\dataset\\7.2.01.tiff')
io.imshow(b)
io.show()

bf = np.float64(b)

b1 = np.uint8(np.clip(bf+50,0,255))
io.imshow(b1)
io.show()

b2 = np.uint8(np.clip(bf-50,0,255))
io.imshow(b2)
io.show()

plt.show()
