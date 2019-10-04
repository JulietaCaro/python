#FUNCION
def devolverDigitos (a, b):
    resto=a%(10**b)
    return resto

#PROGRAMA PRINCIPAL
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
cifras = devolverDigitos(num1, num2)
print(cifras)