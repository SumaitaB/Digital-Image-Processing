import numpy as np
import scipy.ndimage as ndi
import skimage.io as io

#Mean / Average calculation
x=10*np.uint8(np.array([[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]]))
print(x)
print(x[0:3,1:4].mean())


# 3x3 average filtering to 5x5 magic square array
a=np.ones((3,3))/9
print(ndi.convolve(x,a,mode='constant'))



