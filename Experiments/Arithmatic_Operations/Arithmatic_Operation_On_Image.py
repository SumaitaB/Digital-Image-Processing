import skimage.io as io
import matplotlib.pyplot as plt
img = io.imread('U:\\4-1\\Digital Image Processing LAB\\LAB_1(12-04-2022)\\Dataset\\misc\\4.2.05.tiff')
print(type(img))
plt.subplot(2,3,1)
plt.title("Original")
io.imshow(img)

img_add = img + 100
plt.title("Add")
plt.subplot(2,3,2)
io.imshow(img_add)
#io.show()


img_sub = img - 100
plt.title("Sub")
plt.subplot(2,3,3)
io.imshow(img_sub)

img_mul = img * 100
plt.title("Mul")
plt.subplot(2,3,4)
io.imshow(img_mul)

img_div = img / 100
plt.title("Div")
plt.subplot(2,3,5)
io.imshow(img_div)

img_com = 255-img
plt.title("Com")
plt.subplot(2,3,6)
io.imshow(img_com)

io.show()
