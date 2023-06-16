pacientes=[]
for i in range(4):
    paciente={}
    paciente["Nombre"]=input("Ingrese nombre del paciente")
    paciente["Edad"]=input("Ingrese edad del paciente")
    paciente["Peso"]=input("Ingrese peso del paciente")
    sintomas=input("Ingres Sintomas de paciente, separados por una coma")
    paciente["Sintomas"]=sintomas.split(",")
    pacientes.append(paciente)

buscador=input("Ingrese nombre de paciente para encontrar su ficha")
for paciente in pacientes:
    if paciente["Nombre"]==buscador:
        print(paciente["Nombre"])
        print(paciente["Edad"])
        print(paciente["Peso"])
        print(paciente["Sintomas"])
