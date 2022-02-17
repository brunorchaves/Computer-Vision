from PIL import Image
from pylab import *
import numpy as np
from scipy.ndimage import filters
from matplotlib import pyplot as plt
import imtools

# pil_im = Image.open('empire.jpg')

# box = (100,10,400,400)
# region = pil_im.crop(box)
# region = region.transpose(Image.ROTATE_180)
# pil_im.paste(region,box)
# im = array(Image.open('empire.jpg'))
# print( im.shape, im.dtype)

# im2 = 255 - im#invert image
# im3 = (100/255)*im + 100 # clamp to interval 100...200
# im4 = 255.0*(im/255)**2

#create figure
# figure()
# gray()
# contour(im,origin= 'image')

# x = [100,100,400,400]
# y = [200,500,200,500]
# plot(x,y,'r*')

# plot(x[:2],y[:2])
# title('Plotting: "empire.jpg"')
# axis('equal')
# axis('off')

# figure()
# hist(im.flatten(),128)

# im_resized= imtools.imresize(im, uint16)

im = array(Image.open('empire.jpg'))

imx = np.zeros(im.shape,dtype=np.float64)
filters.sobel(im,1,imx)
imy = np.zeros(im.shape,dtype=np.float64)
filters.sobel(im,0,imy)
# imy = zeros(im.shape)
# filters.gaussian_filter(im,(sigma,sigma),(1,0),imy)

magnitude=np.sqrt(imx**2+imy**2)
plt.subplot(2,2,1)
plt.imshow(im,cmap=plt.cm.gray)
plt.title("Original")
plt.subplot(2,2,2)
plt.imshow(magnitude,cmap=plt.cm.gray)
plt.title("Magnitude of Gradient")
plt.subplot(2,2,3)
plt.imshow(imx,cmap=plt.cm.gray)
plt.title('Derivative in x-direction')
plt.subplot(2,2,4)
plt.title('Derivative in y-direction')
plt.imshow(imy,cmap=plt.cm.gray)
plt.show()