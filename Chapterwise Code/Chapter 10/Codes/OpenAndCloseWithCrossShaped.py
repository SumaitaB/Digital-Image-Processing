from skimage.morphology import closing, binary_closing as bwclose, binary_opening as bwopen
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt


cr=np.array([[0,1,0],[1,1,1],[0,1,0]])
test= np.zeros((10,10))
test[1:6,1:4] =1;
test[2:5,5:9]=1;
test[7:9,3:8]=1;
test[3,5]=1;

test_open=bwopen(test,cr)
test_close=bwclose(test,cr)

plt.subplot(2, 3, 1)
plt.title('Original Image')
plt.imshow(test, cmap='gray')
plt.axis('off')


plt.subplot(2, 3, 2)
plt.title('Open')
plt.imshow(test_open, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title('Close ')
plt.imshow(test_close, cmap='gray')
plt.axis('off')


plt.tight_layout()
plt.show()
