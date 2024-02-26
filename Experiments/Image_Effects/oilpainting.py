import cv2
import matplotlib.pyplot as plt
img = cv2.imread('U:\\4-1\\Digital Image Processing LAB\\Chapter_16\\dataset\\iris.jpg')

plt.title('Original Image')
plt.axis('Off')
plt.imshow(img)
plt.show()

res = cv2.xphoto.oilPainting(img, 7, 1)
plt.title('Oil painting')
plt.axis('Off')
plt.imshow(res)
plt.show()
