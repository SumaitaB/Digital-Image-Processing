import numpy as np
import skimage.io as io
from skimage.transform import rescale

r = range(-256, 256)
x, y = np.meshgrid(r, r)
z = np.sqrt(x**2 + y**2)
t = 1 - ((z > 254.5) & (z < 256))
io.imshow(t)
io.show()

t2 = rescale(t, 0.25, order=0)
io.imshow(t2)
io.show()

#t3 = rescale(t, 0.25, order=3)
#t4 = rescale(t, 0.25, order=3) > 0.9
