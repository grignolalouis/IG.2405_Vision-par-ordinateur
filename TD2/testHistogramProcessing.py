# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 12:15:23 2025

@author: fross
"""

import numpy as np
import skimage as ski
import matplotlib.pyplot as plt
import histogramProcessing as hp


# LOAD IMAGE ------------------------------------------------------------------
# im = ski.io.imread("IlesLofoten.png")
im = ski.io.imread("fdoeil.png")
# im = ski.util.img_as_float(im)

print("Image features:")
print("\tData type........:",type(im))
print("\tPixel type.......:",im.dtype)
print('\tGrayscale range..:[',im.min(),',',im.max(),']')
print("\tImage dimension .:",im.ndim)
print("\tImage size.......:",im.shape)
plt.figure()
plt.imshow(im,cmap='gray')
plt.colorbar()
plt.title('Source image')


# TEST myHistogram ------------------------------------------------------------
H0,B0= ski.exposure.histogram(im,256,normalize=True)
H,B = hp.myHistogram(im)
plt.figure()
plt.subplot(1,2,1)
plt.plot(B0,H0)
plt.grid()
plt.title('scikit-image histogram')
plt.subplot(1,2,2)
plt.plot(B,H)
plt.grid()
plt.title('myHistogram histogram')

print('\nEquatity of bins       = '+str(np.array_equal(B0, B)))
print('Equatity of histograms = '+str(np.array_equal(H0, H)))

# TEST myCumulatedHistogram ---------------------------------------------------
HC0,B0= ski.exposure.cumulative_distribution(im,256)
HC,B = hp.myCumulatedHistogram(im)
plt.figure()
plt.subplot(1,2,1)
plt.plot(B0,HC0)
plt.grid()
plt.title('scikit-image distribution')
plt.subplot(1,2,2)
plt.plot(B,HC)
plt.grid()
plt.title('myCumulatedHistogram distribution')

print('\nEquatity of bins       = '+str(np.array_equal(B0, B)))
print('Equatity of histograms = '+str(np.array_equal(np.round(HC0*1e6), (np.round(HC*1e6)))))

# INTENSITY CALIBRATION ------------------------------------------------------
p=0.01
imc = hp.myCalibration(im,p)
print("Calibrated image features:")
print("\tData type........:",type(imc))
print("\tPixel type.......:",imc.dtype)
print('\tGrayscale range..:[',imc.min(),',',imc.max(),']')
print("\tImage dimension .:",imc.ndim)
print("\tImage size.......:",imc.shape)

H,B = hp.myHistogram(im)

plt.figure(figsize=(15,15))
plt.subplot(2,2,1)
plt.imshow(im,cmap='gray')
plt.colorbar()
plt.title('Source image')

plt.subplot(2,2,3)
plt.plot(B,H)
plt.grid()
plt.title('myHistogram histogram')

plt.subplot(2,2,2)
plt.imshow(imc,cmap='gray')
plt.colorbar()
plt.title('Calibrated image')

# Hc,Bc= ski.exposure.histogram(imc,256)
Hc,Bc= hp.myHistogram(imc)
plt.subplot(2,2,4)
plt.plot(Bc,Hc)
plt.title('myHistogram histogram')
plt.grid()
plt.show()

# HISTOGRAM EQUALIZATION ------------------------------------------------------

imc,T = hp.myEqualization(im)
print("Equalized image features:")
print("\tData type........:",type(imc))
print("\tPixel type.......:",imc.dtype)
print('\tGrayscale range..: [{0:.2f} , {1:.2f}]'.format(imc.min(),imc.max()))
print("\tImage dimension .:",imc.ndim)
print("\tImage size.......:",imc.shape)

H,B = hp.myHistogram(im)

plt.figure(figsize=(15,15))
plt.subplot(2,2,1)
plt.imshow(im,cmap='gray')
plt.colorbar()
plt.title('Source image')

plt.subplot(2,2,3)
plt.plot(B,H)
plt.grid()
plt.title('myHistogram histogram')

plt.subplot(2,2,2)
plt.imshow(imc,cmap='gray')
plt.colorbar()
plt.title('Equalized image')


Hc,Bc= hp.myHistogram(imc)
plt.subplot(2,2,4)
plt.plot(Bc,Hc)
plt.title('myHistogram histogram')
plt.grid()
plt.show()

# Compare with scikit-Image
imr  = ski.exposure.equalize_hist(im,256)
imr *= 255
imr  = np.ndarray.astype(imr,np.uint8) 

print("Egalité des images égalisées :",np.array_equal(imc,imr))

