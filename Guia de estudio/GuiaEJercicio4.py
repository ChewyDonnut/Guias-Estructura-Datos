vehiculos=["lamborghini","ferrari","subaru","nissan","ford","porshe"]

def agregar(auto):
    return vehiculos.append(auto)
def invertir():
    return vehiculos.reverse()
def imprimir():
    for i in (vehiculos):
        print(i)
def eliminar_primero():
    return vehiculos.pop(0)
def vaciar():
    return vehiculos.clear()
dato=input("ingrese nuevo vehiculo")
agregar(dato)
eliminar_primero()
print("primer dato eliminado:")
imprimir()

print("datos invertidos:")
invertir()
imprimir()

print("todos los datos eliminados:")
vaciar()
imprimir()

