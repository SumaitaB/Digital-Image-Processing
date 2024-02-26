import numpy as np
import skimage.io as io
import skimage.color as co
import matplotlib.pyplot as plt
rows=7
cols=9
ox = (rows+1)//2
oy = (cols+1)//2
#print(ox,oy)

y,x = np.mgrid[-oy:cols-oy, -ox:rows-ox]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y,x)

#print('r = ',r ,'theta = ',theta)


x2 = np.round(r*np.sin(theta))+ox
y2 = np.round(r*np.cos(theta))+oy

#print('x=',x2)
#print('y=',y2)

# Radial Pixelization


x = np.array( range(1,13) )
#print( np.vstack( (x,x%4) ))

#Sprint(x-x%4)


f = io.imread('U:\\4-1\\Digital Image Processing LAB\\Chapter_16\\dataset\iris.jpg')
fg = co.rgb2gray(f)
#r,theta=polarmesh(fg)

r2 = r - r%5
theta2 = theta - theta%(5*np.pi/180)
x2 = r2*np.cos(theta2)
y2 = r2*np.sin(theta2)

def clip(x,y,z):
    x[np.where(x<y)] = y
    x[np.where(x>y)] = z
    return x

xx = np.round(x2) + ox
yy = np.round(y2) + oy
xx=clip(xx,0,rows-1).astype(int)
yy=clip(yy,0,cols-1).astype(int)


f2 = np.reshape(f[xx.ravel(),yy.ravel()],(rows,cols))
plt.imshow(f2)
plt.show()

