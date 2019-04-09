import numpy as np
import random
from scipy.spatial import Delaunay

#Fonction de création de points aléatoires
def pointsAleatoires(nbPoints, valeurMax):
    listePoints =[]
    n=0
    while(n<nbPoints):
        point = []
        point.append(random.random()* valeurMax)
        point.append(random.random()* valeurMax)
        listePoints.append(point)
        n+=1
    print(listePoints)
    return np.array(listePoints)
    
points = pointsAleatoires(20,10)

#Création des triangles de Delaunay
tri = Delaunay(points)

#Affichage des triangles
import matplotlib.pyplot as plt
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()
