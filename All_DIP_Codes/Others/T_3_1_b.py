import numpy as np
import matplotlib.pyplot as plt
import skimage.filters as fl


img = plt.imread('U:\\4-1\\Digital Image Processing LAB\\DIP_LAB\DIP_LAB\\Dataset\\4.2.07.tiff')

r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

plt.subplot(2,5,1)
plt.axis('off')
plt.title('RGB image')
plt.imshow(img)

plt.subplot(2,5,2)
plt.axis('off')
plt.title('RED component')
plt.imshow(r,cmap='gray')

plt.subplot(2,5,3)
plt.axis('off')
plt.title('GREEN component')
plt.imshow(g,cmap='gray')

plt.subplot(2,5,4)
plt.axis('off')
plt.title('BLUE component')
plt.imshow(b,cmap='gray')

rcon_img = np.dstack((r,g,b))

plt.subplot(2,5,5)
plt.axis('off')
plt.title('Reconstructed color image')
plt.imshow(rcon_img)

edge_r = fl.sobel(r)
edge_g = fl.sobel(g)
edge_b = fl.sobel(b)

plt.subplot(2,5,6)
plt.axis('off')
plt.title('RED componet Edge')
plt.imshow(edge_r, cmap='gray')

plt.subplot(2,5,7)
plt.axis('off')
plt.title('GREEN componet Edge')
plt.imshow(edge_g, cmap='gray')

plt.subplot(2,5,8)
plt.axis('off')
plt.title('BLUE componet Edge')
plt.imshow(edge_b,cmap='gray')


rcon_img_edge = edge_r + edge_g + edge_b

plt.subplot(2,5,9)
plt.axis('off')
plt.title('Reconstructed RGB image edge')
plt.imshow(rcon_img_edge,cmap='gray')

plt.show()

