import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt
from skimage import feature
from skimage import util

c = io.imread('D:\\4-1\\DIP LAB\\dataset\\5.1.12.tiff')
e = feature.canny(c, sigma=2, low_threshold=5)

x, y = np.nonzero(e)
xt = np.array([x]).T
yt = np.array([y]).T
th = np.linspace(0, np.pi, 180)
cos_th = np.array([np.cos(th)])
sin_th = np.array([np.sin(th)])
rtable = np.floor(xt.dot(cos_th)+yt.dot(sin_th))

u = np.unique(rtable)
N = len(u)
hough = np.zeros((N, 180))
for j in range(180):
    for i in range(N):
        hough[i, j] = np.where(rtable[:, j] == u[i])[0].shape[0]

# Display the Hough transform
plt.imshow(hough, cmap='gray', extent=[0, 180, 0, N])
plt.xlabel('Theta (degrees)')
plt.ylabel('Rho')
plt.title('Hough Transform')
plt.show()
