import numpy as np

#Tableau indiquant le nombre de case de la grille sur y et x
size = [10,15]

#Créer un tableau 2D rempli de 0 de la taille du Tableau size
myArray = np.zeros(size)
#Modification de la valeur contenu dans la première case du tableau 2D
myArray[0][0] = 1

#Affiche le tableau 2D
print(myArray, myArray.shape)
