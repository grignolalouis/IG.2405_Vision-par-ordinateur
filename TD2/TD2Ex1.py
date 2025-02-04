# -*- coding: utf-8 -*-
"""
Programme de traitement d'image : Analyse d'histogramme et distribution

Ce script illustre les concepts fondamentaux de l'analyse d'histogramme en traitement d'images :
- Calcul et visualisation de l'histogramme
- Calcul des probabilités de niveaux de gris
- Calcul de la fonction de distribution cumulative

Concepts théoriques :
- Une image en niveaux de gris est une matrice 2D où chaque élément représente 
  l'intensité lumineuse d'un pixel
- Pour une image 8 bits, les valeurs sont comprises entre 0 (noir) et 255 (blanc)
- L'histogramme représente la distribution des niveaux de gris dans l'image
- La fonction de distribution cumulative permet d'analyser la répartition globale 
  des intensités
"""

# IMPORTATION DES BIBLIOTHÈQUES ----------------------------------------------
import numpy as np          # Pour les calculs matriciels
import skimage as ski      # Pour le traitement d'images
import matplotlib.pyplot as plt  # Pour la visualisation

# Configuration de la figure principale pour l'affichage
plt.figure(figsize=(15, 10))

# CHARGEMENT ET ANALYSE DE L'IMAGE -------------------------------------------
"""
Cette section charge l'image et affiche ses caractéristiques techniques.
Propriétés importantes :
- dtype : type de données (uint8 pour 8 bits)
- ndim : nombre de dimensions
- shape : dimensions de l'image (hauteur × largeur)
"""
# Charge l'image depuis le fichier spécifié et la stocke dans une matrice numpy
im = ski.io.imread("TD2/IlesLofoten.png")

# Affiche les caractéristiques techniques de l'image
print("Image features:")
print("\tData type........:", type(im))    # Type de l'objet Python (ndarray)
print("\tPixel type.......:", im.dtype)    # Type des données des pixels (uint8 = 8 bits)
print('\tGrayscale range..:[', im.min(), ',', im.max(), ']')  # Valeurs min et max des pixels
print("\tImage dimension .:", im.ndim)      # Nombre de dimensions (2 pour niveau de gris)
print("\tImage size.......:", im.shape)     # Taille en pixels (hauteur x largeur)

# Configure le premier sous-plot (1er quadrant) pour afficher l'image source
plt.subplot(2, 2, 1)
plt.imshow(im, cmap='gray')        # Affiche l'image en niveaux de gris
plt.colorbar()                     # Ajoute une barre de couleur pour l'échelle
plt.title('Source image')

# CALCUL DE L'HISTOGRAMME ---------------------------------------------------
"""
L'histogramme compte le nombre de pixels pour chaque niveau de gris.
Applications :
- Analyse de la distribution des intensités
- Détection de problèmes de contraste
- Base pour les techniques d'amélioration d'image
"""
# Initialise les variables pour le calcul de l'histogramme
nbGrayLevels = 256                # Nombre de niveaux de gris possibles (8 bits = 2^8)
H, W = im.shape                   # Récupère la hauteur (H) et largeur (W) de l'image

# Crée un tableau pour stocker l'histogramme (compte de pixels par niveau de gris)
Hist = np.zeros(nbGrayLevels)     # Initialise avec des zéros
for i in range(H):                # Parcourt chaque ligne
    for j in range(W):            # Parcourt chaque colonne
        Hist[im[i,j]] += 1        # Incrémente le compteur pour le niveau de gris du pixel

# Affichage de l'histogramme
plt.subplot(2, 2, 2)
plt.bar(range(nbGrayLevels), Hist)    # Crée un graphique en barres de l'histogramme
plt.title('My histogram')
plt.xlabel('gray levels')              # Axe X : niveaux de gris (0-255)
plt.ylabel('# pixels')                 # Axe Y : nombre de pixels
plt.grid(True)                         # Ajoute une grille pour meilleure lisibilité

# CALCUL DES PROBABILITÉS --------------------------------------------------
"""
La probabilité P(i) pour chaque niveau de gris i est :
P(i) = nombre de pixels de niveau i / nombre total de pixels

Propriétés :
- 0 ≤ P(i) ≤ 1
- La somme de toutes les probabilités = 1

Applications :
- Base pour l'égalisation d'histogramme
- Analyse statistique de l'image
"""
# Calcule les probabilités en normalisant l'histogramme
P = Hist / (H * W)                     # Divise par le nombre total de pixels

# Affichage des probabilités
plt.subplot(2, 2, 3)
plt.bar(range(len(P)), P)              # Crée un graphique en barres des probabilités
plt.title("Probabilities of gray levels")
plt.xlabel("Gray levels")               # Axe X : niveaux de gris
plt.ylabel("Gray level probabilities")  # Axe Y : probabilités (entre 0 et 1)
plt.grid(True)

# Calcule un exemple de probabilité cumulative jusqu'au niveau 100
n = 100                                # Niveau de gris choisi pour l'exemple
pn = np.sum(P[0:n])                    # Somme des probabilités de 0 à n
print('Probability that a pixel has a gray level less or equal than ', n, ' = {0:.2f}'.format(pn))

# CALCUL DE LA FONCTION DE DISTRIBUTION -------------------------------------
"""
La fonction de distribution cumulative F(k) est la somme des probabilités 
jusqu'au niveau k.

Propriétés :
- F(k) = Σ P(i) pour i de 0 à k
- F est monotone croissante
- 0 ≤ F(k) ≤ 1

Applications :
- Égalisation d'histogramme
- Analyse de la répartition des niveaux de gris
- Base pour les transformations d'intensité
"""
# Initialise le tableau pour la fonction de distribution cumulative
F = np.zeros(len(P))                   # Crée un tableau de zéros de même taille que P
for k in range(len(P)):                # Pour chaque niveau de gris
    F[k] = np.sum(P[0:k+1])           # Somme toutes les probabilités jusqu'à k

# Affichage de la fonction de distribution
plt.subplot(2, 2, 4)
plt.plot(range(len(P)), F)             # Trace la fonction de distribution cumulative
plt.title('Gray level distribution function')
plt.xlabel('Gray levels')
plt.ylabel('Cumulative probability')
plt.grid(True)

# Optimisation de l'affichage
plt.tight_layout()
plt.show()