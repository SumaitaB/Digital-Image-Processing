import skimage.io as io
from skimage.viewer import ImageViewer as IV
from skimage.color import rgb2gray

img = io.imread('U:\\4-1\\Digital Image Processing LAB\\LAB_1(12-04-2022)\\Dataset\\misc\\4.2.07.tiff')

img_gray = rgb2gray(img)

viewer = IV(img_gray)

viewer.show()

