from numpy import random
import numpy  as np
# matriz=[];size=3
# for i in range(size):
#     aux=[]
#     for j in range(size):
#         aux.append(random.randint(5,10))
#     matriz.append(aux)
matriz=random.randint(3,9,size=(3,3))

for a in matriz:
    print(a)
determiante=round(np.linalg.det(matriz))
print(determiante)