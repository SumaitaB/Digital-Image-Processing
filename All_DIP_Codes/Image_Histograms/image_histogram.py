import skimage.io as io
import matplotlib.pyplot as plt

img = io.imread('U:\\4-1\\Digital Image Processing LAB\\LAB_1(12-04-2022)\\Dataset\\misc\\7.2.01.tiff')

plt.imshow(img)

f = plt.figure()

f.show(plt.hist(img.flatten(), bins=256))

plt.show()
