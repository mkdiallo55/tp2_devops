# Pourquoi numpy?
    # manipulation des données en grande quantité et de sources tres varié
    # présenté généralement sous forme de listes ou tableaux de nombres
# Problématique : les objets natifs de python sont assez limités pour les manipuler correctement 
# Numpy est une bibliotheque qui fournit des operations sur les donnees 
    # mais egalement un objet au coeur de l'ecosysteme data en python:l'array
# 1. le tableau numpy ou array?
    # similaire a une liste python mais permet d'effectuer simplement et rapidement de nombreuses operations
    # faciliter le stockage et la manipulation des donnees
# dans un premier temps installons numpy
    # pip install numpy
# importons numpy
import numpy as np
# 3.creation d'array Numpy
revenus = [1800, 1500 , 1200, 2200, 4568, 4568]
revenus_array = np.array(revenus)
print(revenus_array)
# autres methode pour la creation de tableau numpy
tab1 = np.array([[1, 2],
                [3, 4],
                [5, 6]])
tab2 = np.array([[1, 2, 3],
                [4, 5, 6]])
print(tab1)
    # si le tableau contient des int et des float numpy essaiera de les convertir en float
    # pour respecter le principe du meme type pour tous les valeurs de l'array
# d'autres fonctions numpy permettant de creer des tableaux
    # np.zeros(n) # permet de créer un array rempli de 0, de n éléments
    # np.ones(n) # similaire en tous points à la fonction présentée ci-dessus, à la différence que l’array sera rempli cette fois-ci de 1
    # np.arange(i, j, p) # permet de créer un array rempli avec une séquence linéaire, qui ira de  i  à  j, par pas de  p
    # np.linspace(i, j, n) # permet de créer un array de  n  valeurs espacées uniformément entre  i  et  j.
print(np.ones((3, 5))) # un tableau de taille 3x5 rempli de 1
print(np.zeros((4, 4))) # creation de tableau de taille 4x4 contenant que des 0
print(np.random.random((6, 3))) # creation de tableau de taille 6x3 # un tableau de 6x3 rempli de valeurs aléatoires comprises entre 0 et 1
print(np.random.randint(1, 10, size=(3,3))) #un tableau de 3x3 rempli de valeurs aléatoires entières, comprises entre 1 et 10
print(np.empty(2)) # creation de tableau non initialisé de deux valeur (les valeurs sont aleatoires)
print(np.arange(2, 6, 2)) # creation de commencant par 2 jusqu'a 6 exclu avec un pas de 2

# comme un array dans numpy est monotype on peut acceder au type des elements via la methode .dtype
print(revenus_array.dtype)
# acces au elements d'un array se fait via la syntaxe nom_array[indice] a noter que les indices commencant de 0 a n
print(revenus_array[3]) # pour acceder au 4ième element
print(revenus_array[-1]) # pour acceder au dernier element
revenus_array[-1] = 1900 # pour modifier la valeur du dernier element de l'array
print(revenus_array)
print(revenus_array[0:2]) # pour acceder aux elements de l'indice 0 a 2
print(revenus_array[:3]) # pour afficher les 3 premiers elements de l'array
print(revenus_array[1:]) # pour afficher a partir de l'indice 1
print(revenus_array[::2]) # pour afficher un element sur 2
print(revenus_array[::-2]) # excellent moyen pour inverser un tableau si le pas est negatif
# acces a plusieurs elements selon une condition
    # de la meme facon qu'il est possible de selectionner des elements via leur indice il est possible egalement avec les  arrays numpy de renseigner la condition 
    # selon laquelle on souhaite  selectionner les elements du tableau
print(revenus_array[(revenus_array > 2000) & (revenus_array < 3000)])
# il est egalement possible  de le complexifier avec plusieurs conditions
revenus_array[revenus_array > 2000 ] = 0 # pour remplacer par 0 tous les elements ssuperieur a 2000
# manipulation de tableau
    # la fonction np.reshape(a, (taille matrice))
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([15, 16,17])
c = np.array([[15, 16, 17],
             [1, 12, 13]])
print(np.reshape(a, (2,3))) # remodeler le tableau a en une matrice de taille 2x3
print(np.concatenate(a, b)) # permet de concatener deux tableaux
print(np.split(a, 3)) # permet de subdiviser un tableau a en 3 sous tableaux
print(np.transpose(c)) # permet de transposer un tableau a dimension 2 plus
# les methodes d'array
print(revenus_array.shape) # pour obtenir le nombre d'element de l'array
revenus_array.mean() # pour calculer la moyenne
print(revenus_array.max()) # pour obtenir le maximun d'un array
print(revenus_array.min()) # pour avoir le minimum de l'array
revenus_array.argmin() # pour obtenir l'indice de l'element minimum
revenus_array.argmax() # pour obtenir l'indice de l'element maximum
revenus_array.sort() # ordonner par ordre croissant
print(revenus_array.sum()) # pour calculer la somme

# d'autres fonctions mathematiques de numpy:
x = [-2, -1, 1, 2]
print("La valeur absolue: ", np.abs(x)) # permet de calculer la valeur absolue d'un nombre
print("Exponentielle: ", np.exp(x)) # permet de calculer l'exponentielle d'un nombre
print("Logarithme: ", np.log(np.abs(x))) # permet de calculer le logarithme
print(np.cos(90))
print(np.sin(90))
print(np.log(1))
# analogie entre les arrays et les matrices
    # Le but premier de NumPy, avant même toutes ses applications dans le domaine de la data, est de proposer des outils 
    # pour manipuler ces matrices et effectuer ce qu’on appelle des calculs matriciel
# possibilité de d'additionner des matrices avec numpy exemple:
A = np.array([[1, 2], [3, 4]]) # creation de la matrice A
B = np.array([[5, 10], [15, 20]]) 
C = np.array([[2, 4, 6], [8, 10, 12]]) 
print(A+B) # somme de matrice
print(A*B) # muplication de matrice
print(np.linalg.inv(A)) # permet de calculer l'inverse d'une matrice
print(np.linalg.det(A)) # permet de calculer le determinant d'une matrice
# produit matriciel
    # le produit matriciel se fait via l'operateur @ mais cet operateur n'est disponible que depuis python 3.5
print(A @ C)
    # mais aussi avec la fonction dot de numpy
AC = np.dot(A, C)
print(AC)
