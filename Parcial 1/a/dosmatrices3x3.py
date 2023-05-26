from numpy import random
import numpy as np
matriz1=random.randint(-10,-5,size=(3,3))
matriz2=random.randint(-10,-5,size=(3,3))
multiplicacion=np.matmul(matriz1,matriz2)
print("multiplicacion \n",multiplicacion)
for a in matriz1:
    print(a)
print("saltp")
for a in matriz2:
    print(a)    