#FUNCIONES
def multiplicacion(nroA, nroB):
    i = nroB
    multipli = 0
    while i > 0:
        multipli = multipli + nroA
        i = i - 1
    return multipli
def elevado(nroA, nroB):
    i = nroB
    multipl = 1
    while i > 0:
        multipl = multipl * nroA
        i = i - 1
    return multipl

def separarDigitos(num):
    cifra1 = numero//10
    cifra2 = numero % 10
    return cifra1, cifra2

#PROGRAMA PRINCIPAL
numero = int(input("Ingrese un numero: "))
while numero < 10 or numero > 99:
    numero = int(input("Error, reingrese un numero: "))
while numero != -1:
    primerDigito, segundoDigito = separarDigitos(numero)
    if primerDigito > segundoDigito:
        multipli = multiplicacion(primerDigito, segundoDigito)
        print("Multiplicacion de las cifras: ", multipli)
    if segundoDigito > primerDigito or primerDigito == segundoDigito:
        exponente = elevado(segundoDigito, primerDigito)
        print("Exponente: ", exponente)
    numero = int(input("Ingrese otro numero: "))
