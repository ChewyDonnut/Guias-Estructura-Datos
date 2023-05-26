from numpy import random
import numpy as np

matriz=random.randint(5,10,size=(3,3))
print(np.linalg.det(matriz))
print(matriz)
