#FUNCIONES
def mayor(numeroA, numeroB):
    if numeroA > numeroB:
        mayor = numeroA
    else:
        mayor = numeroB
    return mayor
#PROGRAMA PRINCIPAL
cantidad = int(input("Ingrese la cantidad de numeros a ingresar: "))
while cantidad < 1:
    cantidad = int(input("Error, reingrese la cantidad de numeros a ingresar: "))
cont = 0
suma = 0
while cont < cantidad:
    primerNum = int(input("Ingrese un numero: "))
    segundoNum = int(input("Ingrese otro numero: "))
    mayorNum = mayor(primerNum, segundoNum)
    suma = suma + mayorNum
    cont = cont + 1
    
promedio = suma // cantidad
print("Promedio de los numeros mayores: ", promedio)