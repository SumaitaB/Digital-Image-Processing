import numpy as np
from numpy.fft import fft

x = np.array([2, 3, 4, 5, 6, 7, 8, 1])
x1 = x.copy()
x1[1::2] = x1[1::2] * -1
L = fft(x)
L1 = fft(x1)

print("Original Array x:")
print(x)

print("Modified Array x1:")
print(x1)

print("Fourier Transform of x (L):")
for val in L:
    print("{:.4f} + {:.4f}i".format(val.real, val.imag))

print("Fourier Transform of x1 (L1):")
for val in L1:
    print("{:.4f} + {:.4f}i".format(val.real, val.imag))
