import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import feature
from skimage import transform

c = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.1.12.tiff')
e = feature.canny(c)

rad = transform.radon(e)

# Display the Radon transform
plt.imshow(rad, cmap='gray')
plt.xlabel('Theta (degrees)')
plt.ylabel('Projection axis')
plt.title('Radon Transform')
plt.show()
