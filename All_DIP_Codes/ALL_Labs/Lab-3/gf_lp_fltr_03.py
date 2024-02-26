import numpy as np
import skimage.io as io
import skimage.data as data
import scipy.ndimage as ndi

img01= data.camera()

io.imshow(img01)
io.show()

img02= ndi.gaussian_filter(img01,5,truncate=3)

io.imshow(img02)
io.show()
