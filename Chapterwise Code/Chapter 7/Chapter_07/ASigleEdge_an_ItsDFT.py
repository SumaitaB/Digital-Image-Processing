import numpy as np
import matplotlib.pyplot as plt

# Define the edge position
edge_position = 128

# Create the image with a single edge and black border
a = np.hstack([np.zeros((256, 128)), np.ones((256, 128))])

# Add a black border around the image
border_width = 2
a[:border_width, :] = 0
a[-border_width:, :] = 0
a[:, :border_width] = 0
a[:, -border_width:] = 0

# Compute the 2D Fourier Transform of the image
dft = np.fft.fftshift(np.fft.fft2(a))

# Display the image and its DFT
plt.subplot(1, 3, 1)
plt.imshow(a, cmap='gray')
plt.title('Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(np.abs(dft), cmap='gray')
plt.title('DFT')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(np.log(1+abs(dft)), cmap='gray')
plt.title('Log_scaling')
plt.axis('off')

plt.tight_layout()
plt.show()
