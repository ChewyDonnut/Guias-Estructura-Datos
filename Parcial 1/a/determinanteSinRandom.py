import numpy as np
matriz=[]
for i in range(3):
    aux=[]
    for j in range(3):
        aux.append(int(input(f"ingrese dato de matriz {[i],[j]}")))
    matriz.append(aux)
print("determinante: ",round(np.linalg.det(matriz)))
for row in matriz:
    print(row)