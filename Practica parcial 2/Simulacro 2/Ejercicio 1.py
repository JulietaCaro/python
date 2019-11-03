import random
#FUNCIONES
def generarListaRandom(cantidad):
    cont = 0
    listaRandom = []
    while cont < cantidad:
        numero = random.randint(1, 1000)
        listaRandom.append(numero)
        cont = cont + 1
    return listaRandom

def buscarDato(lista, dato):
    i = 0
    while i < len(lista) and lista[i] != dato:
        i = i + 1
    if i == len(lista):
        encontrado = False
    else:
        encontrado = True
    return encontrado

def insertarDato(lista, dato):
    lista.append(0)
    for i in range(1, len(lista)):
        valorInsertar = dato
        j = i
    while j>0:
        lista[j] = lista[j-1]
        j = j - 1
    lista[j] = valorInsertar
    return lista

def menorNumero(lista):
    menor = lista[0]
    for i in range (0, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor

def cambiarMenor(lista, menor):
    cont = 0
    for i in range (1, len(lista)):
        if lista[i] == menor:
            aux = lista[i]
            lista[i] = lista[i-1]
            lista[i-1] = aux
            cont = cont + 1
    return lista, cont
    
#PROGRAMA PRINCIPAL
cantElementos = int(input("Ingrese la cantidad de elementos a crear: "))
while cantElementos < 0:
    cantElementos = int(input("Error, reingrese la cantidad de elementos: "))

listaRandom = generarListaRandom(cantElementos)

dato = int(input("Ingrese un dato: "))
while buscarDato(listaRandom, dato)==True:
    dato = int(input("Ingrese otro dato: "))

listaInsertada = insertarDato(listaRandom, dato)
print("Lista con numero agregado: ", listaInsertada)
menorNum = menorNumero(listaInsertada)
print("Menor: ", menorNum)
listaCambiada, cambios = cambiarMenor(listaInsertada, menorNum)
print("Lista cambiada: ", listaCambiada)
print("Se realizaron",cambios,"cambio/s")