# -*- coding: utf-8 -*-
"""
Ce script illustre le traitement d'images couleur et leur conversion en niveaux de gris
"""

# Import des bibliothèques nécessaires
import numpy as np          # Pour les calculs matriciels
import skimage as ski      # Pour le traitement d'images
import matplotlib.pyplot as plt  # Pour l'affichage des images

"""
SECTION 1: CHARGEMENT D'UNE IMAGE RGB
Une image RGB (Red Green Blue) est composée de 3 canaux de couleur.
Chaque pixel est représenté par 3 valeurs entre 0 et 255.
"""

# Charge l'image 'fleur.jpg' depuis le dossier TD1
im = ski.io.imread('TD1/fleur.jpg')

# Affiche l'image dans une nouvelle figure
plt.figure()
plt.imshow(im)

# Affiche les informations sur l'image
print("Type de l'image : ", im.dtype)    # Type des données (uint8 = entiers 0-255)
print("Dimensions      : ", im.ndim)     # Nombre de dimensions (3 pour RGB)
print("Taille          : ", im.shape)    # Taille (hauteur, largeur, canaux)

"""
SECTION 2: SÉPARATION DES CANAUX RGB
On extrait chaque canal de couleur pour les visualiser séparément.
"""

# Récupère les dimensions de l'image
H,W,P = im.shape

# Extrait chaque canal de couleur
R = im[:,:,0]  # Canal rouge (première composante)
G = im[:,:,1]  # Canal vert (deuxième composante)
B = im[:,:,2]  # Canal bleu (troisième composante)

# Affiche les 3 canaux côte à côte
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(R,cmap='gray')  # Affiche le canal R en niveaux de gris
plt.title('Canal R')
plt.subplot(1,3,2)
plt.imshow(G,cmap='gray')  # Affiche le canal V en niveaux de gris
plt.title('Canal V')
plt.subplot(1,3,3)
plt.imshow(B,cmap='gray')  # Affiche le canal B en niveaux de gris
plt.title('Canal B')
plt.show()

"""
SECTION 3: CONVERSION EN NIVEAUX DE GRIS
Il existe plusieurs méthodes pour convertir une image couleur en niveaux de gris:
1. Moyenne pondérée des canaux (formule standard)
2. Moyenne simple des canaux (moins précise)
3. Fonction intégrée de scikit-image
"""

# Méthode 1: Conversion avec la formule standard
# Ces coefficients prennent en compte la sensibilité de l'œil aux différentes couleurs
img = 0.299*R + 0.587*G + 0.114*B  

# Méthode 2 (en commentaire): Moyenne simple des canaux
# img = (R + G + B)/3  

# Affiche les résultats des deux méthodes de conversion
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img,cmap = 'gray')
plt.title('Ma conversion')
print("Type de l'image : ", img.dtype)    # Le type change car résultat d'opérations flottantes
print("Dimensions      : ", img.ndim)     # 2 dimensions car image en niveaux de gris
print("Taille          : ", img.shape)    # Plus que hauteur et largeur (plus de canaux)

# Méthode 3: Utilisation de la fonction intégrée de scikit-image
img2 = ski.color.rgb2gray(im)
plt.subplot(1,2,2)
plt.imshow(img2,cmap = 'gray')
plt.title('scikit-Image conversion')
print("Type de l'image : ", img2.dtype)
print("Dimensions      : ", img2.ndim)
print("Taille          : ", img2.shape)

# Compare si les deux conversions donnent le même résultat
print('img2 = img :' + str(np.array_equal(img,img2)))


