#FUNCION
def esPar(a):
    if a % 2 == 0:
        par = True
    else:
        par = False
    return par

#PROGRAMA PRINCIPAL
numero = int(input("Ingrese un numero: "))
num = esPar(numero)
print(num)