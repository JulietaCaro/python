#FUNCIONES
def esPar(nro):
    if nro %2 == 0:
        esPar = True
    else:
        esPar = False
    return esPar

#PROGRAMA PRINCIPAL
contPar = 0
suma = 0
numero = int(input("Ingrese un numero: "))
while numero != -1:
    if esPar(numero):
        contPar = contPar + 1
        suma = suma + numero
    numero = int(input("Ingrese otro numero: "))
print("Numero pares: ", contPar)
print("Suma de los numeros pares: ", suma)
