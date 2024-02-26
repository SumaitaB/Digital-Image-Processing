import numpy as np

a = range(1, 7)
L = np.fft.fft(a)

for x in L:
    print('%0.4f%+0.4fi' % (x.real, x.imag))
