#FUNCION
def concatenar (a, b):
    a = str(a)
    b = str(b)
    concatenado = a+b
    return concatenado
    
#PROGRAMA PRINCIPAL
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
conca = concatenar(num1, num2)
print(conca)