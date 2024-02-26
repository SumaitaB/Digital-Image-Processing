import numpy as np
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import skimage.data as data

#Let an image matrix = img
img = data.camera()
plt.title('Original Image')
plt.axis('OFF')
plt.imshow(img)
plt.show()

head = img[
            50 : 150, # height
            151 : 255 # weight
           ]

#Get rows and columns from matrix, m
rows, cols = head.shape

#Increase double size of m(4x4) whch is m2(8x8)
m2 = np.zeros( (2*rows, 2*cols) )

m2[ : : 2, : : 2] = head

print(m2)
plt.title('Zero Interleaved')
plt.axis('OFF')
plt.imshow(m2)
plt.show()

#Filter for Nearest Neighbor Interpolation
mask1 =np.array([
                [0, 0, 0],
                [0, 1, 1],
                [0, 1, 1]
                ]) 
#Filter for Bilinear Interpolation
mask2 =np.array([
                [1, 2, 1],
                [2, 4, 2],
                [1, 2, 1]
                ])/4.0 
#Filter for Bicubic Interpolation
mask3 = np.array([
                [1, 4, 6, 4, 1],
                [4, 16, 24, 16, 4],
                [6, 24, 36, 24, 6],
                [4, 16, 24, 16, 4],
                [1, 4, 6, 4, 1],
                ])/64.0 

filtered_img1 = ndi.convolve(m2, mask1, mode = 'constant')
filtered_img2 = ndi.convolve(m2, mask2, mode = 'constant')
filtered_img3 = ndi.convolve(m2, mask3, mode = 'constant')

plt.title('After Nearest Neighbor Interpolation')
plt.axis('OFF')
plt.imshow(filtered_img1)
plt.show()

plt.title('After Bilinear Interpolation')
plt.axis('OFF')
plt.imshow(filtered_img2)
plt.show()

plt.title('After Bicubic Interpolation')
plt.axis('OFF')
plt.imshow(filtered_img3)
plt.show()
