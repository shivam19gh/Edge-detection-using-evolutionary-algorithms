from __future__ import division
from gaussian_filter import gaussian
from gradient import gradient
from nonmax_suppression import maximum
from numpy import array, zeros, max
from PIL import Image
from matplotlib.pyplot import imshow, show, subplot, figure, gray, title, axis

def thresholding(im):
    thres  = zeros(im.shape)
    strong = 1.0
    weak   = 0.5
    mmax = max(im)
    lo, hi = 0.1 * mmax, 0.8 * mmax
    strongs = []
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            px = im[i][j]
            if px >= hi:
                thres[i][j] = strong
                strongs.append((i, j))
            elif px >= lo:
                thres[i][j] = weak
    return thres, strongs

if __name__ == '__main__':
    from sys import argv
    
    im = array(Image.open("1.jpeg"))
    im = im[:, :, 0]
    gim = gaussian(im)
    grim, gphase = gradient(gim)
    gmax = maximum(grim, gphase)
    thres = thresholding(gmax)
    gray()

    subplot(2, 3, 1)
    imshow(im)
    axis('off')
    title('Original')

    subplot(2, 3, 2)
    imshow(gim)
    axis('off')
    title('Gaussian')

    subplot(2, 3, 3)
    imshow(grim)
    axis('off')
    title('Gradient')

    subplot(2, 3, 4)
    imshow(gmax)
    axis('off')
    title('Non-Maximum suppression')

    subplot(2, 3, 6)
    imshow(thres[0])
    axis('off')
    title('Double thresholding')

    show()
