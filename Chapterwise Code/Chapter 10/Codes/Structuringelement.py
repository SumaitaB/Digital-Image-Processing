import skimage.io as io
import numpy as np
from scipy import ndimage as ndi
from skimage.morphology import square

A = np.array([[10, 20, 20, 20, 30],
              [20, 30, 30, 40, 50],
              [20, 30, 30, 40, 50],
              [20, 30, 30, 50, 60],
              [20, 40, 50, 50, 60],
              [30, 50, 60, 60, 70]]).astype('uint')

struct = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(ndi.grey_erosion(A, footprint=square(3), structure=struct))


struct2=np.array([[9, 8, 7],
                   [6, 5, 4],
                   [3, 2, 1]])

print(ndi.grey_erosion(A, footprint=square(3), structure=struct))
