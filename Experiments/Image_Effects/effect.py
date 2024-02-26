import cv2 
import numpy as np
import random
import math
color_image = cv2.imread("U:\\4-1\\Digital Image Processing LAB\\Chapter_16\\dataset\\iris.jpg")  
cv2.imshow("Flower",color_image)  
cv2.waitKey()  
cv2.destroyAllWindows()
cartoon_image = cv2.stylization(color_image, sigma_s=150, sigma_r=0.25)  
cv2.imshow('cartoon', cartoon_image)  
cv2.waitKey()  
cv2.destroyAllWindows()
cartoon_image1, cartoon_image2  = cv2.pencilSketch(color_image, sigma_s=60, sigma_r=0.5, shade_factor=0.02)
cv2.imshow('pencil', cartoon_image2)    
cv2.waitKey()    
cv2.destroyAllWindows() 
height, width, channels = color_image.shape

# Randomly select a point in the 10x10 range of the lower right for each point
# mm is the value range, the bigger the wider
mm = 10
for i in range(0, height):
    for j in range(0, width):
        # Random points
        r = int(random.random() * mm)
        r_i, r_j = i + r, j + r
        # Handling out of bounds
        if r_i >= height:
            r_i = height - 1
        elif r_i < 0:
            r_i = 0 
        if r_j >= width:
            r_j = width - 1
        elif r_j < 0:
            r_j = 0
        # Modify pixels
        color_image[i, j] = color_image[r_i, r_j]

cv2.imshow("img", color_image)
if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
