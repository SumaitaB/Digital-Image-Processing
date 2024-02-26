import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
from skimage.transform import rotate

# Load the image
c = io.imread('D:\\4-1\\DIP LAB\\dataset\\cameraman.jpg')

# Rotate the image by 60 degrees using nearest-neighbor interpolation (order=0)
cr = rotate(c, angle=60, order=0, mode='constant', cval=0)

# Display the rotated image using io.imshow
io.imshow(cr)
plt.show()

# Rotate the image by 60 degrees using bicubic interpolation (order=3)
crc = rotate(c, angle=60, order=3, mode='constant', cval=0)

# Display the rotated image using plt.imshow
plt.figure()
plt.imshow(crc)
plt.show()
