#FUNCIONES
import random
def crearListaRandom():
    listaRandom = []
    numero = random.randint(0, 100)
    while numero != 0:
        listaRandom.append(numero)
        numero = random.randint(0, 100)
    return listaRandom

def promedio(listaRandom):
    acum = 0
    for i in range(0, len(listaRandom)):
        acum = acum + listaRandom[i]
    if acum == 0:
        promedio = 0
    else:
        promedio = acum // len(listaRandom)
    return promedio

def elementosMayoresAlPromedio(lista, promedio):
    listaMayores = []
    posiciones = []
    for i in range(0, len(lista)):
        if lista[i] > promedio:
            listaMayores.append(lista[i])
            posiciones.append(i)
    return listaMayores, posiciones

def eliminarValoresImpares(lista):
    i = len(lista)-1
    cont = 0
    while i >= 0:
        if lista[i] % 2 != 0:
            lista.pop(i)
            cont = cont + 1
        i = i - 1
    return lista, cont

#PROGRAMA PRINCIPAL
listaRandom = crearListaRandom()
print("Elementos creados: ", len(listaRandom))
print("Lista: ", listaRandom)
promedioLista = promedio(listaRandom)
print("Promedio de la lista: ", promedioLista)
mayores, posMayores = elementosMayoresAlPromedio(listaRandom, promedioLista)
for i in range(0, len(mayores)):
    print("Mayor al promedio:",mayores[i],"Posicion:",posMayores[i])
print("Lista original: ", listaRandom)
listaSinImpares, valoresElimi = eliminarValoresImpares(listaRandom)
print("Lista sin impares: ", listaSinImpares)
print("Valores eliminados: ", valoresElimi)

   