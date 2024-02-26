import numpy as np
import matplotlib.pyplot as plt

img1 = plt.imread('U:\\4-1\\Digital Image Processing LAB\\LAB_1(12-04-2022)\\Dataset\\misc\\4.1.04.tiff')


r = img1[:, :, 0]
g = img1[:, :, 1]
b = img1[:, :, 2]

output = [img1, r, g, b]
titles = ['Image', 'Red', 'Green', 'Blue']

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.axis('off')
    plt.title(titles[i])
    if i == 0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i], cmap='gray')

plt.show()

output = np.dstack((r, g, b))

plt.imshow(output)
plt.show()
