import skimage.data as data
import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np

def unsharp(alpha=0.2):
    A1 = np.array([
                  [-1,1,-1],
                  [1,1,1],
                  [-1,1,-1]
                    ])
    A2 = np.array([
        [0,-1,0],
        [-1,5,-1],
        [0,-1,0]
        ])
    return (alpha*A1+A2)/(alpha+1)

p = np.array([
    [100,400,34,89,20],
    [98,32,56,90,23],
    [67,87,20,55,68],
    [32,90,56,77,44],
    [87,45,90,43,20]
    ])

plt.imshow(p)
plt.show()

u = unsharp(0.5)
pu = ndi.convolve(p.astype(float),u)

plt.imshow(pu/255,vmax=1.0, vmin=0.0)
plt.show()
