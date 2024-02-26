import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray, rgb2hsv
from matplotlib.colors import hsv_to_rgb

# Read the image and convert it to grayscale
img_01 = plt.imread('C:\\Dataset\\4.2.07.tiff')
img_gray = rgb2gray(img_01)

# Convert the RGB image to HSV
Ihsv = rgb2hsv(img_01)

# Separate the RGB channels
r = img_01[:, :, 0]
g = img_01[:, :, 1]
b = img_01[:, :, 2]

z_r = np.zeros_like(r)
z_g = np.zeros_like(g)
z_b = np.zeros_like(b)

# Create separate color channel images
r_img = np.dstack((r, z_g, z_b))
g_img = np.dstack((z_r, g, z_b))
b_img = np.dstack((z_r, z_g, b))

# Separate the H, S, and V channels
H = Ihsv[:, :, 0]
S = Ihsv[:, :, 1]
V = Ihsv[:, :, 2]

# Reconstruct the RGB image from the separated channels
rcon_img = np.dstack((H, S, V))
rcon_img = hsv_to_rgb(rcon_img)

# Display the images in subplots
plt.figure(figsize=(20, 10))

# Original RGB image
plt.subplot(2, 5, 1)
plt.axis('off')
plt.title('Color image')
plt.imshow(img_01)

# Separate R, G, B channels
plt.subplot(2, 5, 2)
plt.axis('off')
plt.title('RED channel image')
plt.imshow(r, cmap='gray')

plt.subplot(2, 5, 3)
plt.axis('off')
plt.title('GREEN channel image')
plt.imshow(g, cmap='gray')

plt.subplot(2, 5, 4)
plt.axis('off')
plt.title('BLUE channel image')
plt.imshow(b, cmap='gray')

# Reconstructed RGB image
plt.subplot(2, 5, 5)
plt.axis('off')
plt.title('Reconstructed color image')
plt.imshow(rcon_img)

# Separate H, S, V channels
plt.subplot(2, 5, 6)
plt.axis('off')
plt.title('Hue channel')
plt.imshow(H, cmap='gray')

plt.subplot(2, 5, 7)
plt.axis('off')
plt.title('Saturation channel')
plt.imshow(S, cmap='gray')

plt.subplot(2, 5, 8)
plt.axis('off')
plt.title('Value channel')
plt.imshow(V, cmap='gray')

# Add HSV reconstructed image
plt.subplot(2, 5, 9)
plt.axis('off')
plt.title('HSV Reconstructed image')
plt.imshow(rcon_img)

plt.show()
