# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:41:27 2024

@author: fross
"""

import numpy as np
import skimage as ski
import matplotlib.pyplot as plt

# Charger l'image
im = ski.io.imread('texte.png')
im =  -- to be completed    # transform to float

print("Image features:")
print("\tData type........:",type(im))
print("\tPixel type.......:",im.dtype)
print('\tGrayscale range..: [{0:.2f} , {1:.2f}]'.format(im.min(),im.max()))
print("\tImage dimension .:",im.ndim)
print("\tImage size.......:",im.shape)

H,W=im.shape
fig = plt.figure(figsize=(15,12))
plt.subplot(3,1,1)
plt.imshow(im,cmap='gray')
plt.colorbar()

# Calculer le profil cumulé vertical
profV= -- to be completed 
plt.subplot(3,1,2)
plt.plot(range(len(profV)),profV)
plt.title('Profil vertical cumulé')
plt.grid(True)

# Calculer le profil cumulé horizontal
profH=-- to be completed 
plt.subplot(3,1,3)
plt.plot(range(len(profH)),profH)
plt.title('Profil horizonal cumulé')
plt.grid(True)
plt.show()

# Déterminer les séparations entre les caractères
# un caractère commence quand le profil passe d'une valeur basse à une valeur 
# supérieure à un seuil T, et se termine quand il repasse à une valeur inférieure

-- to be completed 

