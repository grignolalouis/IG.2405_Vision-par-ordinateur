# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:56:27 2025

@author: fross
"""

import numpy as np
import skimage as ski
import matplotlib.pyplot as plt



# LOAD IMAGE ------------------------------------------------------------------
im = ski.io.imread("fdoeil.png")

plt.figure(figsize=(45,15))
plt.subplot(1,2,1)
plt.imshow(im,cmap='gray')
plt.colorbar()
plt.title('Source image')


print("Image features:")
print("\tData type........:",type(im))
print("\tPixel type.......:",im.dtype)
print('\tGrayscale range..:[',im.min(),',',im.max(),']')
print("\tImage dimension .:",im.ndim)
print("\tImage size.......:",im.shape)

# COMPUTE HISTOGRAM -----------------------------------------------------------

Hist0, Bins0 = -- to be completed


plt.subplot(1,2,2)
plt.plot(Bins0,Hist0)
plt.title("Histogram - scikit-Image")
plt.xlabel('gray levels')
plt.ylabel('# pixels')
plt.grid(True)
plt.show()


# CALIBRATE -------------------------------------------------------------------

minVal = -- to be completed   
maxVal = -- to be completed
imc = -- to be completed
imc = np.ndarray.astype(imc,np.uint8)

Hist, Bins = ski.exposure.histogram(imc,nbins=256,normalize=True ) 
plt.figure(figsize=(45,15))
plt.subplot(1,2,2)
plt.plot(Bins,Hist)
plt.title("Histogram after calibration")
plt.xlabel('gray levels')
plt.ylabel('# pixels')
plt.grid(True)
plt.subplot(1,2,1)
plt.imshow(im,cmap='gray')
plt.colorbar()
plt.title('After calibration')

imc2 = ski.exposure.rescale_intensity(-- to be completed)
print('Egalité des images = ' + str(np.array_equal(imc,imc2)))


# CALIBRATE WITH p% OF SATURATION ---------------------------------------------
HistC,BinsC = ski.exposure.cumulative_distribution(im,nbins=-- to be completed)
plt.figure()
plt.subplot(1,2,1)
plt.imshow(im,cmap='gray')
plt.title('Before calibration')
plt.subplot(1,2,2)
plt.plot(BinsC,HistC)
plt.title("Cumulative distribution")
plt.xlabel('gray levels')
plt.ylabel('# pixels')
plt.grid(True)

p = 0.01
ind = np.argwhere(-- to be completed)
minVal = -- to be completed
maxVal = -- to be completed
print("Range for a {0:.2f} % saturation = [{1} ,  {2}]".format(p*100,minVal,maxVal) )

imc = np.ndarray.astype(im,np.int64)
imc = np.round(-- to be completed)   # apply calibration given minVal and maxVal
imc = np.maximum(imc,-- to be completed)
imc = np.minimum(imc,-- to be completed)
imc = np.ndarray.astype(imc,np.uint8)


Hist, Bins = ski.exposure.histogram(imc,nbins=256,normalize=True ) 
plt.figure()
plt.subplot(1,2,2)
plt.plot(Bins,Hist)
plt.title("Histogram after calibration with  {0:.2f} % saturation".format(p*100))
plt.xlabel('gray levels')
plt.ylabel('# pixels')
plt.grid(True)
plt.subplot(1,2,1)
plt.imshow(imc,cmap='gray')
plt.title('After calibration')


# USE scikit-Image
imc2 = ski.exposure.rescale_intensity(im,(-- to be completed,-- to be completed),(-- to be completed,-- to be completed))
imc2 = np.round(imc2)
imc2 = np.ndarray.astype(imc2,np.uint8)

print('Egalité des images = ' + str(np.array_equal(imc,imc2)))
plt.figure(figsize=(35,15))
plt.subplot(1,2,1)
plt.imshow(imc,cmap='gray')
plt.title("My calibration with  {0:.2f} % saturation".format(p*100))
plt.subplot(1,2,2)
plt.imshow(imc2,cmap='gray')
plt.title("scikit-Image calibration with  {0:.2f} % saturation".format(p*100))
