#FUNCIONES
def cantidadDigitos(numero):
    cont = 0
    while numero > 0:
        numero = numero //10
        cont = cont + 1
    return cont

def digitoCentral(numero):
    digitos = cantidadDigitos(numero)
    central = digitos // 2
    for i in range(central):
        numero = numero // 10
    digito = numero % 10
    return digito

def ordenarMenorAMayor(listaSocios, listaHoras, listaDigito):
    for i in range(0, len(listaDigito)):
        for j in range(i+1, len(listaDigito)):
            if listaDigito[i] > listaDigito[j]:
                aux = listaDigito[i]
                listaDigito[i] = listaDigito[j]
                listaDigito[j] = aux
                
                aux = listaSocios[i]
                listaSocios[i] = listaSocios[j]
                listaSocios[j] = aux
                
                aux = listaHoras[i]
                listaHoras[i] = listaHoras[j]
                listaHoras[j] = aux
                
def buscarSocio(lista, socio):
    encontrado = False
    i = 0
    while i < len(lista) and encontrado == False:
        if lista[i] == socio:
            encontrado = True
        i = i + 1
    return encontrado

def sumarHoras(listaSocios, listaHoras, socio):
    suma = 0
    for i in range(len(listaSocios)):
        if listaSocios[i] == socio:
            suma = suma + listaHoras[i]
    return suma

def mostrarCodigosYHoras(listaSocios, listaHoras):
    listaSociosAux = []
    for i in range(0, len(listaSocios)):
        if buscarSocio(listaSociosAux, listaSocios[i])==False:
            listaSociosAux.append(listaSocios[i])
            suma = sumarHoras(listaSocios, listaHoras, listaSocios[i])
            print("Socio:",listaSocios[i],"Dias:",suma//24,"Horas:",suma%24)
    
#PROGRAMA PRINCIPAL
listaSocios = []
listaHoras = []
listaDigitoCentral = []
numeroSocio = int(input("Ingrese un numero de socio: "))
while (cantidadDigitos(numeroSocio) % 2 == 0) and numeroSocio != -1:
    numeroSocio = int(input("Eror, reingrese un numero de socio: "))
while numeroSocio != -1:
    hora = int(input("Ingrese las horas: "))
    while hora < 1 or hora > 24:
        hora = int(input("Error, reingrese las horas:"))
    
    listaSocios.append(numeroSocio)
    #busco el digito central del numero de socio
    digiCentral = digitoCentral(numeroSocio)
    #guardo el digito central del numero de socio
    listaDigitoCentral.append(digiCentral)
    listaHoras.append(hora)
    
    numeroSocio = int(input("Ingrese un numero de socio: "))
    while (cantidadDigitos(numeroSocio) % 2 == 0) and numeroSocio != -1:
        numeroSocio = int(input("Eror, reingrese un numero de socio: "))

ordenarMenorAMayor(listaSocios, listaHoras, listaDigitoCentral)
print()
print("SOCIOS ORDENADOS POR DIGITO CENTRAL")
for i in range(len(listaSocios)):
    print("Socio:",listaSocios[i],"Hora:",listaHoras[i])
print()
print("SOCIOS SIN REPETIR")
mostrarCodigosYHoras(listaSocios, listaHoras)