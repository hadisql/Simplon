#https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1?

## PSEUDO-CODE : 
# On fait du récursif : 
# si l'entrée est une matrice 1x1 : on ajoute le dernier terme à la liste + FIN
# si l'entrée est une matrixe NxN : on fait le tour façon snake

import numpy as np

def snail(snail_map):
    #print(snail_map)
    snail_map = np.array(snail_map)
    if len(snail_map)==0:
        return snail_map.tolist()
    elif len(snail_map)==1:
        return snail_map[0].tolist()
    else:
        L = len(snail_map) - 1
        return np.concatenate((snail_map[0,:],snail_map[1:,L],
                               np.flip(snail_map[L,:L]),
                               np.flip(snail_map[1:L,0]),
                               snail(snail_map[1:-1,1:-1])),axis=0).tolist()


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(snail(array))
