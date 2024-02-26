import numpy as np
import skimage.io as io
import scipy.ndimage as ndi

def unsharp(alpha=0.2):
    A1=np.array([[-1,1,-1],[1,1,1],[-1,1,-1]])
    A2=array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    return (alpha*A1+A2)/(alpha+1)

img01= io.imread('E://4-1//406 DIP Lab//DIP_LAB//Dataset//7.2.01.tiff')
io.imshow(img01)
io.show()

u=unsharp(0.5)
ku=ndi.convolve(img01.astype(float),u)
io.imshow(ku/255,vmax=1.0,vmin=0.0)
io.show()
