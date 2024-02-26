import skimage.io as io
from skimage.viewer import ImageViewer as IV
from skimage.color import rgb2hsv

img = io.imread('D:\\Dataset\\4.2.07.tiff')

img_hsv = rgb2hsv(img)

viewer = IV(img_hsv)

viewer.show()

