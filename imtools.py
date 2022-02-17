import os
from PIL import Image
from pylab import *
import numpy

def get_imlist(path):
    """" Retruns a list of filenames for
    all jpg images in a dorectory"""
    return[os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

from numpy import array, uint8

# resize any image
def imresize(im,sz):
    pil__im = Image.fromarray(uint8(im))
    return array(pil__im.resize(sz))


## gives more details , more contrast, good for usage before further processing
def histeq(im, nbr_bins = 256):
    #"""" Histogram equalization of a grayscale image"""
    #get image histogram
    imhist, bins = histogram(im.flatten(),nbr_bins,density = True)
    cdf = imhist.cumsum() #cumukatuve distribution function
    cdf = 255*cdf / cdf[-1]#normalize
    #use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(),bins[:-1],cdf)

    return im2.reshape(im.shape),cdf

def compute_average(imlist):
    """Compute the average of a list of images"""
    #open first image and make into array of type float
    averageim = array(Image.open[0],'f')

    for imname in imlist[1:]:
        try :
            averageim += array(Image.open(imname))
        except:
            print(imname + '...skiped')
    averageim /= len(imlist)

    #return average as uint8
    return array(averageim,'uint8')