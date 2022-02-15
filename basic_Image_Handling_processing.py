from PIL import Image
from pylab import *
import numpy

# pil_im = Image.open('empire.jpg')

# box = (100,10,400,400)
# region = pil_im.crop(box)
# region = region.transpose(Image.ROTATE_180)
# pil_im.paste(region,box)
im = array(Image.open('empire.jpg'))
print( im.shape, im.dtype)
im = array(Image.open('empire.jpg').convert('L'),'f')
print( im.shape, im.dtype)

im2 = 255 - im#invert image
im3 = (100/255)*im + 100 # clamp to interval 100...200
im4 = 255.0*(im/255)**2

#create figure
figure()
gray()
contour(im,origin= 'image')

# x = [100,100,400,400]
# y = [200,500,200,500]
# plot(x,y,'r*')

# plot(x[:2],y[:2])
# title('Plotting: "empire.jpg"')
axis('equal')
axis('off')

figure()
hist(im.flatten(),128)
show()