#FUNCION
def comparar (a, b):
    if a > b:
        nro = 1
    else:
        if a == b:
            nro = 0
        else:
            nro = -1
    return nro
    
#PROGRAMA PRINCIPAL
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
compar = comparar (num1, num2)
print(compar)