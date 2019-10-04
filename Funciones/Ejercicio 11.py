#FUNCION
def raiz(a):
    raizCuadrada = a**(1/2)
    return raizCuadrada

#PROGRAMA PRINCIPAL
num = int(input("Ingrese un numero: "))
if num > 0:
    resultado = raiz(num)
    print("Raiz cuadrada: %.2f" %resultado)