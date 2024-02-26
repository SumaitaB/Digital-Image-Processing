import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

C = np.convolve(a, np.hstack([b, b]), 'valid')[:-1]
print("C:", C)

fft_result1 = np.fft.fft(C)
print("Fourier Transform of C:")
print(fft_result1)

fft_result2 = np.fft.fft(a) * np.fft.fft(b)
print("Product of Fourier Transforms of a and b:")
print(fft_result2)

ab = np.fft.fft(a) * np.fft.fft(b)
ifft_result = np.fft.ifft(ab).real
print("Real part of the inverse Fourier Transform of ab:")
print(ifft_result)
