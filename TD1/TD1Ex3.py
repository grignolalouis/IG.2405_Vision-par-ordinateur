# -*- coding: utf-8 -*-
"""
Exercice 3: Manipulation d'images en niveaux de gris
Ce script illustre différentes techniques de manipulation d'images en niveaux de gris:
- Chargement et conversion d'images
- Modification de pixels
- Seuillage d'images
- Utilisation de masques
"""

import numpy as np
import skimage as ski
import matplotlib.pyplot as plt

"""
SECTION 1: CHARGEMENT ET ANALYSE D'UNE IMAGE
"""
# Charge l'image test 'cameraman' intégrée dans skimage
im = ski.data.camera()

# Affiche les informations sur l'image
print("Informations sur l'image chargée:")
print("type de im:", type(im))           # Type de l'objet (numpy array)
print("\tType des éléments:", im.dtype)  # Type des pixels (uint8)
print('\tIntervalle des valeurs:[', im.min(), ',', im.max(), ']')  # Valeurs min/max
print("\tDimension:", im.ndim)           # Nombre de dimensions
print("\tTaille:", im.shape)             # Dimensions de l'image

# Affiche l'image avec une barre de couleur
plt.figure(figsize=(15,5))
plt.imshow(im, cmap='gray')
plt.colorbar()  # Ajoute une barre montrant la correspondance valeurs/couleurs
plt.title('Cameraman')
plt.show()

"""
SECTION 2: CONVERSION EN FLOAT64
Les calculs sont plus précis avec des nombres flottants
"""
# Convertit l'image en float64 (valeurs entre 0 et 1)
im2 = ski.util.img_as_float(im)

# Affiche les nouvelles informations
print("Informations sur l'image convertie:")
print("type de im2:", type(im2))
print("\tType des éléments:", im2.dtype)
print('\tIntervalle des valeurs:[', im2.min(), ',', im2.max(), ']')
print("\tDimension:", im2.ndim)
print("\tTaille:", im2.shape)
plt.imshow(im2, cmap='gray')
plt.show()

"""
SECTION 3: MODIFICATION DE PIXELS
Exemple: création d'un rectangle blanc dans l'image
"""
# Crée une copie de l'image pour ne pas modifier l'originale
im3 = im.copy()
# Définit les coordonnées du rectangle
i1, i2 = 100, 200  # Lignes de début et fin
j1, j2 = 350, 400  # Colonnes de début et fin
# Met les pixels du rectangle à blanc (255 en uint8)
im3[i1:i2, j1:j2] = 255  
plt.imshow(im3, cmap='gray')
plt.show()

"""
SECTION 4: SEUILLAGE D'IMAGE
Le seuillage est une opération fondamentale en traitement d'image qui permet de 
créer une image binaire (noir et blanc) à partir d'une image en niveaux de gris.

Principe du seuillage:
- On choisit une valeur seuil T (entre 0 et 1 pour une image en float)
- Pour chaque pixel:
    * Si sa valeur > T → pixel devient blanc (1.0)
    * Si sa valeur ≤ T → pixel devient noir (0.0)

Applications courantes:
- Segmentation d'objets
- Détection de contours
- Création de masques binaires
- Réduction du bruit

Deux méthodes de seuillage sont présentées:
1. Méthode avec boucles (intuitive mais lente)
2. Méthode vectorisée avec numpy (rapide et concise)
"""

# Charge une nouvelle image de test
im = ski.data.page()
im = ski.util.img_as_float(im)
im4 = np.empty_like(im)  # Crée une image vide de même taille
H,W = im4.shape
T = 0.3   # Valeur de seuil (à ajuster selon l'image)

"""
Méthode 1: Seuillage avec boucles
Avantages:
- Code explicite et facile à comprendre
- Permet de voir le processus pixel par pixel
Inconvénients:
- Très lent sur de grandes images
- Non optimisé pour Python/NumPy
"""
#for i in range(H):
#    for j in range(W):
#        if im[i,j] > T:
#            im4[i,j] = 1.0  # Pixel blanc
#        else:
#            im4[i,j] = 0.0  # Pixel noir

"""
Méthode 2: Seuillage vectorisé avec NumPy
Avantages:
- Beaucoup plus rapide (jusqu'à 100x)
- Code plus concis
- Utilise les optimisations de NumPy
Inconvénients:
- Syntaxe moins intuitive pour les débutants
"""
# La comparaison (im > T) crée un masque booléen
# astype(float) convertit True en 1.0 et False en 0.0
im4 = (im > T).astype(float)

# Affichage des résultats
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.imshow(im, cmap='gray')
plt.title('Image originale')
plt.subplot(1,2,2)
plt.imshow(im4, cmap='gray')
plt.title('Image seuillée (T = {})'.format(T))
plt.show()

"""
Note sur le choix du seuil:
- Un seuil trop bas inclura trop de pixels (bruit)
- Un seuil trop haut perdra des informations importantes
- Le choix optimal dépend de:
    * Le contenu de l'image
    * L'application visée
    * La distribution des niveaux de gris
    * Le niveau de bruit

Pour un seuillage plus avancé, on peut utiliser:
- Seuillage adaptatif (seuil variable selon la zone)
- Méthode d'Otsu (calcul automatique du seuil optimal)
- Multi-seuillage (plus de 2 classes)
"""

"""
SECTION 5: UTILISATION DE MASQUES
Application de masques pour modifier des zones spécifiques
"""
# Charge une image de chat et la convertit en niveaux de gris
im = ski.data.cat()
im = ski.color.rgb2gray(im)
T = 0.3
im5 = im.copy()

# Crée et applique un masque basé sur un seuil
masque = im > T  # Masque booléen
im5[masque] = 0  # Met à noir les pixels où masque est True

# Création d'un masque circulaire avec mgrid
H,W = im.shape
G = np.mgrid[0:H,0:W]  # Crée des grilles de coordonnées
X = G[0,:,:]-H/2      # Coordonnées X centrées
Y = G[1,:,:]-W/2      # Coordonnées Y centrées
R = np.sqrt(X**2+Y**2)  # Calcul des distances au centre
R0 = 0.4*min(H,W)      # Rayon du cercle
masque = R > R0         # Masque circulaire


# Application du masque circulaire
im7 = im.copy()
im7[masque] = 0  # Noir à l'extérieur du cercle
plt.figure() 
plt.imshow(im7,cmap='gray') 
plt.title('Image avec masque circulaire') 
plt.show()
# Création d'un spot lumineux

"""
SECTION 5: CRÉATION D'UN SPOT LUMINEUX
Création d'un effet de spot lumineux centré sur le nez du chat
"""
# Charge et convertit l'image du chat
im = ski.data.cat()
im = ski.color.rgb2gray(im)

# Coordonnées approximatives du nez du chat
H, W = im.shape
center_y = 190  # Position verticale du nez
center_x = 240  # Position horizontale du nez

# Création de la grille de coordonnées centrée sur le nez
G = np.mgrid[0:H, 0:W]
X = G[0,:,:]-H/2      # Coordonnées X centrées
Y = G[1,:,:]-W/2      # Coordonnées Y centrées
R = np.sqrt(X**2+Y**2)  # Calcul des distances au centre
R0 = 0.4*min(H,W)      # Rayon du cercle
sigma = 50  # Contrôle la douceur de la transition

# Création du masque avec dégradé
gradient = np.exp(-((R - R0)**2) / (2*sigma**2))  # Fonction gaussienne
gradient = np.clip(gradient, 0.2, 1.0)  # Limite l'assombrissement

# Application du spot
im_spot = im.copy()
im_spot = im_spot * gradient  # Multiplication par le gradient

# Affichage des résultats
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(im, cmap='gray')
plt.title('Image originale')

plt.subplot(1,3,2)
plt.imshow(gradient, cmap='gray')
plt.title('Masque avec dégradé')

plt.subplot(1,3,3)
plt.imshow(im_spot, cmap='gray')
plt.title('Image avec spot lumineux')
plt.show()


