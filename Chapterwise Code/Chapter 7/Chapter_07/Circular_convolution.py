import numpy as np

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

conv_result = np.convolve(a, b)
print("Convolution of a and b:")
print(conv_result)

valid_conv_result = np.convolve(a, b + b, 'valid')[:-1]
print("Valid Convolution of a and b+b:")
print(valid_conv_result)
