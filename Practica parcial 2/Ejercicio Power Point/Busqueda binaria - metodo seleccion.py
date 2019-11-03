#FUNCIONES
def ordenarListas(listaLegajos, listaNotas):
    for i in range(0, len(listaLegajos)-1):
        for j in range(i+1, len(listaLegajos)):
            if listaLegajos [i] < listaLegajos[j]:
                aux = listaLegajos[i]
                listaLegajos[i]= listaLegajos[j]
                listaLegajos[j] = aux
                
                aux = listaNotas[i]
                listaNotas[i] = listaNotas[j]
                listaNotas[j] = aux

def mayorNota(listaNotas):
    mayor = 0
    for i in range(0, len(listaNotas)):
        if listaNotas[i]> mayor:
            mayor = listaNotas[i]
    return mayor

def legajosDeNotaMayor(listaLegajos, listaNotas, mayor):
    listaLegajosMayores = []
    for i in range(0, len(listaNotas)):
        if listaNotas[i] == mayor:
            listaLegajosMayores.append(listaLegajos[i])
    return listaLegajosMayores       
 
def ordenarListasAscendente(listaLegajos, listaNotas):
    for i in range(0, len(listaLegajos)-1):
        for j in range(i+1, len(listaLegajos)):
            if listaLegajos [i] > listaLegajos[j]:
                aux = listaLegajos[i]
                listaLegajos[i]= listaLegajos[j]
                listaLegajos[j] = aux
                
                aux = listaNotas[i]
                listaNotas[i] = listaNotas[j]
                listaNotas[j] = aux
 
def busquedaBinaria(listaLegajos, listaNotas, legajoABuscar):
    izq = 0
    dere = len(listaLegajos)-1
    pos = -1
    while izq <= dere and pos == -1:
        centro = (izq + dere)//2
        if listaLegajos[centro] == legajoABuscar:
            pos = centro
        elif listaLegajos[centro] < legajoABuscar:
            izq = centro + 1
        else:
            dere = dere - 1
    
    if pos == -1:
        nota = -1
    else:
        nota = listaNotas[pos]
    return nota
#PROGRAMA PRINCIPAL
listaLegajos = []
listaNotas = []
cont = 0
cantidadAlumnos = int(input("Ingrese la cantidad de alumnos: "))
while cantidadAlumnos < 0:
    cantidadAlumnos = int(input("Error, reingrese la cantidad de alumnos: "))
while cont < cantidadAlumnos:
    legajo = int(input("Ingrese el legajo del alumno: "))
    while legajo < 0:
        legajo = int(input("Error, reingrese el legajo del alumno: "))
    nota = int(input("Ingrese la nota del alumno: "))
    while nota < 1 or nota > 10:
        nota = int(input("Error, reingrese la nota del alumno: "))
    listaLegajos.append(legajo)
    listaNotas.append(nota)
    cont = cont + 1
    
ordenarListas(listaLegajos, listaNotas)
for i in range(0, len(listaLegajos)):
    print("Legajo:",listaLegajos[i],"Nota:",listaNotas[i])
    
notaMayor = mayorNota(listaNotas)
print("Mayor nota: ", notaMayor)
legajosNotaMayor = legajosDeNotaMayor(listaLegajos, listaNotas, notaMayor)
print("Legajos con la mayor nota: ", legajosNotaMayor)
legajoABuscar = int(input("Ingrese un legajo a buscar: "))
ordenarListasAscendente(listaLegajos, listaNotas)
nota = busquedaBinaria(listaLegajos, listaNotas, legajoABuscar)
if nota == -1:
    print("No existe el legajo",legajoABuscar)
else:
    print("Nota: ",nota)