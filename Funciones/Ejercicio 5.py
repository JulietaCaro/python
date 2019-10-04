#FUNCION
def maximo (a, b):
    if a > b:
        maximo = a
    else:
        maximo = b
    return maximo

#PROGRAMA PRINCIPAL
numA = int(input("Ingrese un numero: "))
numB = int(input("Ingrese otro numero: "))
mayor = maximo (numA, numB)
print("El mayor es: ", mayor)