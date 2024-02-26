from wand.image import Image
import matplotlib.pyplot as plt
import numpy as np 
# Read image using Image function
with Image(filename ="U:\\4-1\\Digital Image Processing LAB\\Chapter_16\\dataset\\iris.jpg") as img:
    plt.title('Original Image')
    plt.axis('Off')
    plt.imshow(img)
    plt.show()
    # rippled image using vignette() function
    img1=img.wave(amplitude = img.height / 24,
             wave_length = img.width / 8)
    img.save(filename ="U:\\4-1\\Digital Image Processing LAB\\Chapter_16\\dataset\\ripplediris.jpg")
    
with Image(filename ="U:\\4-1\\Digital Image Processing LAB\\Chapter_16\\dataset\\ripplediris.jpg") as output:
    plt.title('Rippled Image')
    plt.axis('Off')
    plt.imshow(output)
    plt.show()


