from numpy import random
import numpy  as np

matriz1=random.randint(-10,-5,size=(3,3))
matriz2=random.randint(-10,-5,size=(3,3))
mi=[[1,0,0],[0,1,0],[0,0,1]]
matriz3=np.matmul(matriz1,matriz2)
matriz4=np.matmul(matriz3,mi)


print("matriz resultado: \n",matriz3)

print("matriz resultado2: \n",matriz4)
