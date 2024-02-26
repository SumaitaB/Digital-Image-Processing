import numpy as np
import matplotlib.pyplot as plt

a = np.array([0, 100, 150, 255])
b = np.array([40, 100, 220, 255])
lin = np.interp(range(256), a, b)

f = plt.figure()
plt.hist(lin.flatten(), bins=256)
plt.show()
