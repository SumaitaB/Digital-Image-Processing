import cv2
import numpy as np
import skimage.io as io
import skimage.exposure as ex
import matplotlib.pyplot as plt

img01= io.imread('D:\\4-1\\DIP LAB\\dataset\\5.3.01.tiff')
io.imshow(img01)
io.show()

f = plt.figure()
f.show(plt.hist(img01.flatten(), bins=256))
plt.show()

img02 = cv2.equalizeHist(img01)   
io.imshow(img02)
io.show()

f = plt.figure()
f.show(plt.hist(img02.flatten(), bins=256))
plt.show()
