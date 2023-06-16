documentos=["informe","Guia de estudio","tesis 4","seminario osorno"]
def imprimir():
    print(documentos)
def apilar(dato):
    documentos.append(dato)
def top():
    return print("el elemento top es: ",documentos[-1])
def is_empty():
    return  len(documentos)==0

imprimir()
apilar("avance Tesis")
apilar("proyecto integrador")

top()
eliminado=documentos.pop()
print("el elemento eliminado es: ",eliminado)
imprimir()
print("la lista esta vacia?",is_empty())