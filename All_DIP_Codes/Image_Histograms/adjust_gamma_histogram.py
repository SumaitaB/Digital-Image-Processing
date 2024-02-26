import skimage.io as io
import matplotlib.pyplot as plt
import skimage.exposure as ex

img01= io.imread('U:\\4-1\\Digital Image Processing LAB\\LAB_1(12-04-2022)\\Dataset\\misc\\7.2.01.tiff')

plt.imshow(img01)
plt.show()

img02= ex.adjust_gamma(img01,0.5)

io.imshow(img02)
io.show()

f = plt.figure()

f.show(plt.hist(img02.flatten(), bins=256))

plt.show()
