# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:56:27 2025

@author: fross
"""

import numpy as np
import skimage as ski
import matplotlib.pyplot as plt


# LOAD IMAGE ------------------------------------------------------------------
im = ski.io.imread("IlesLofoten.png")
# im = ski.io.imread("fdoeil.png")

plt.figure()
plt.subplot(1,2,1)
plt.imshow(im,cmap='gray')
plt.colorbar()
plt.title('Source image')


print("Image features:")
print("\tData type........:",type(im))
print("\tPixel type.......:",im.dtype)
print('\tGrayscale range..: [{0:.2f} , {1:.2f}]'.format(im.min(),im.max()))
print("\tImage dimension .:",im.ndim)
print("\tImage size.......:",im.shape)



# COMPUTE EQUALIZATION TRANSFORM-----------------------------------------------

N=256 
H,W = im.shape
P = np.zeros(N)
T = --to be completed
    
    
plt.figure()
plt.plot(range(N),T)
plt.grid()
plt.title('Equalization transform')
plt.show()
   
    
# EQUALIZE IMAGE --------------------------------------------------------------

ime = --to be completed
 

# DISPLAY --------------------------------------------------------------------- 
plt.figure(figsize=(45,30))
plt.subplot(2,3,1)
plt.imshow(im,cmap='gray')
plt.title('Before equalization')
plt.subplot(2,3,2)
P,B = ski.exposure.histogram(im,normalize=True)
plt.plot(B,P)
plt.title('Probabilities')
plt.grid()
plt.subplot(2,3,3)
F,B = ski.exposure.cumulative_distribution(im)
plt.plot(B,F)
plt.title('Distribution function')
plt.grid()

plt.subplot(2,3,4)
plt.imshow(ime,cmap='gray')
plt.title('After equalization')
plt.subplot(2,3,5)
P,B = ski.exposure.histogram(ime,normalize=True)
plt.plot(B,P)
plt.title('Probabilities')
plt.grid()
plt.subplot(2,3,6)
F,B = ski.exposure.cumulative_distribution(ime)
plt.plot(B,F)
plt.title('Distribution function')
plt.grid()
plt.show()

# # COMPARE WITH SCIKIT-IMAGE ---------------------------------------------------
imr  = -- to be completed


print("Egalité des images égalisées :",np.array_equal(ime,imr))







