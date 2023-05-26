import random
m1=[]
m2=[]
mi=[[1,0,0],[0,1,0],[0,0,1]]
# se crean las matrices 1 y 2
for i in range(3):
    aux=[]
    aux2=[]
    for j in range(3):
        aux.append(random.randint(-10,-5))
        aux2.append(random.randint(-10,-5))
    m1.append(aux)
    m2.append(aux2)
#transpuesta matriz 1
m1t=[]
for i in range(3):
    auxi=[]
    for j in range(3):
        auxi.append(m1[j][i])
    m1t.append(auxi)

#multiplicar transpuesta 1 y matriz 2
mr=[]
for i in range(3):
    aux=[]
    for j in range(3):
        suma=0
        for k in range(3):
            suma+=(m1t[i][k]*m2[k][j])
        aux.append(suma)
    mr.append(aux)
#transpuesta de mr
mrt=[]
for i in range(3):
    auxi=[]
    for j in range(3):
        auxi.append(mr[j][i])
    mrt.append(auxi)
#multiplicacion de transpuesta de resultado y matriz identidad
mri=[]
for i in range(3):
    aux=[]
    for j in range(3):
        suma=0
        for k in range(3):
            suma+=(mr[i][k]*mi[k][j])
            
        aux.append(suma)
    mri.append(aux)
   
print("matriz1")
for a in m1:
    print(a)
print("matriz 1 transpuesta")
for a in m1t:
    print(a)
print("matriz2")
for a in m2:
    print(a)

print("matriz resultante de matriz 1 * matriz 2")
for a in mr:
    print(a)
print("resultante transpuesta")
for a in mrt:
    print(a)

print("matriz resultante de matriz resultado transpuesta * matriz identidad")
for a in mri:
    print(a)


