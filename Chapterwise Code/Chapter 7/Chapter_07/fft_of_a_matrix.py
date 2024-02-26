import numpy as np

a1 = np.ones((8, 8))
a2 = np.array([[100, 200], [100, 200]])
a2 = np.tile(a2, (4, 4))
a3 = np.hstack([np.zeros((8, 4)), np.ones((8, 4))])

fft_result1 = np.fft.fft2(a1).astype(np.int16)
print("2D Fourier Transform of a1:")
print(fft_result1)

print("a2:")
print(a2)

fft_result2 = np.fft.fft2(a2).astype(np.int16)
print("2D Fourier Transform of a2:")
print(fft_result2)

print("a3:")
print(a3)

af3 = np.fft.fftshift(np.fft.fft2(a3))
fft_shift_result = np.round(np.abs(af3), 0).astype(np.int16)
print("2D Fourier Transform of a3 after shift and rounding:")
print(fft_shift_result)
