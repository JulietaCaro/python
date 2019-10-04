#FUNCION
def multiplicacion (a, b):
    acum = 1
    for i in range (1, (b+1)):
        acum = acum * a
#    print(acum)
    return acum

#PROGRAMA PRINCIPAL
primerNumero = int(input("Ingrese un numero: "))
segundoNumero = int(input("Ingrese otro numero: "))
multi = multiplicacion (primerNumero, segundoNumero)
print(multi)