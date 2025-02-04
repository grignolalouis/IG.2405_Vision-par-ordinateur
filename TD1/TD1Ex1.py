# -*- coding: utf-8 -*-
"""
modifié le 01/02/2025 par LOUIS GRIGNOLA    
Programme de traitement d'image : manipulation des tables de couleurs
"""

# IMPORTATION DES BIBLIOTHÈQUES -----------------------------------------------------
# NumPy : bibliothèque pour le calcul numérique, permet de manipuler des tableaux multidimensionnels
import numpy as np          
# Scikit-image : bibliothèque spécialisée dans le traitement d'images
import skimage as ski      
# Matplotlib : bibliothèque de visualisation, sous-module pyplot pour l'affichage
import matplotlib.pyplot as plt  
# ListedColormap : classe permettant de créer des palettes de couleurs personnalisées
from matplotlib.colors import ListedColormap  

"""
COURS : Une image numérique en niveaux de gris est une matrice 2D où chaque élément
représente l'intensité lumineuse d'un pixel. Pour une image 8 bits, les valeurs 
sont comprises entre 0 (noir) et 255 (blanc).
"""

# CHARGEMENT ET ANALYSE DE L'IMAGE ------------------------------------------------
# Lecture de l'image depuis le fichier - retourne un tableau NumPy
im = ski.io.imread("TD1/autumng.png")  

# Affichage des caractéristiques techniques de l'image
print("Informations sur l\'image chargée:")
print("type de im:",type(im))           # Affiche le type d'objet (numpy.ndarray)
print("\tType des éléments:",im.dtype)  # Type des pixels (uint8 = entiers 8 bits)
print('\tIntervalle des valeurs:[',im.min(),',',im.max(),']')  # Valeurs extrêmes
print("\tDimension:",im.ndim)           # Nombre de dimensions de l'image
print("\tTaille:",im.shape)             # Dimensions en pixels (hauteur, largeur)

"""
COURS : L'affichage d'une image nécessite une table de correspondance (LUT - Look-Up Table)
qui définit comment les valeurs numériques sont converties en couleurs à l'écran.
"""

# AFFICHAGE DE L'IMAGE ORIGINALE -------------------------------------------------
plt.imshow(im,cmap='gray')              # Affiche l'image avec la palette de gris standard
plt.colorbar()                          # Ajoute une barre montrant la correspondance valeurs/couleurs
plt.show()                              # Affiche la figure créée

# ANALYSE D'UN PIXEL SPÉCIFIQUE -------------------------------------------------
i=62                                    # Coordonnée ligne (axe vertical, de haut en bas)
j=121                                   # Coordonnée colonne (axe horizontal, de gauche à droite)
print("La valeur du pixel de coordonnées (",i,",",j,") est :",im[i,j])

"""
COURS : La quantification réduit le nombre de niveaux de gris utilisés pour représenter l'image.
Cela peut créer un effet de "posterisation" où les transitions douces deviennent plus brutales.
"""

# QUANTIFICATION EN 16 NIVEAUX --------------------------------------------------
nbCouleurs = 16                         # Définit le nombre de niveaux de gris désirés
myColors = np.zeros((nbCouleurs,3),float)  # Crée une table vide (nbCouleurs lignes, 3 colonnes RGB)

# Remplit la table des couleurs avec un dégradé de gris
for p in range(3):                      # Pour chaque canal (R,G,B)
    myColors[:,p] = np.linspace(0,1,nbCouleurs)  # Crée une progression linéaire de 0 à 1

newcmp = ListedColormap(myColors)       # Crée une nouvelle palette à partir de la table
plt.figure()                            # Crée une nouvelle fenêtre d'affichage
plt.imshow(im,cmap=newcmp)             # Affiche l'image avec la nouvelle palette
plt.colorbar()                          # Ajoute la barre de correspondance
plt.title('Affichage sur '+ str(nbCouleurs) + ' couleurs')  # Titre explicatif
plt.show()                              # Affiche le résultat

"""
COURS : Les fausses couleurs consistent à représenter les intensités de gris avec des
couleurs différentes pour mettre en évidence certaines caractéristiques de l'image.
"""

# CRÉATION DES FAUSSES COULEURS ------------------------------------------------
nbCouleurs = 256                        # Retour à 256 niveaux pour plus de finesse
myColors = np.zeros((nbCouleurs,3),float)  # Nouvelle table de couleurs

# Création du dégradé initial
for p in range(3):                      # Pour chaque canal (R,G,B)
    myColors[:,p] = np.linspace(0,1,nbCouleurs)  # Dégradé linéaire de base

# Modification des canaux pour créer l'effet de fausses couleurs
myColors[-128:,0] = 1.0                 # Met le canal rouge au maximum pour les valeurs hautes

newcmp = ListedColormap(myColors)       # Crée la palette de fausses couleurs
plt.figure()                            # Nouvelle fenêtre
plt.imshow(im,cmap=newcmp)             # Applique la palette
plt.colorbar()                          # Barre de correspondance
plt.title('Affichage avec dominante rouge')  # Titre explicatif
plt.show()                              # Affiche le résultat
