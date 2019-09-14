cont = 0
contador = 1
acumulador = 0
cantidad = int(input("Ingrese la cantidad a generar: "))
while cantidad < 0:
    cantidad = int(input("Error, ingrese la cantidad a generar: "))
while cont < cantidad:
    print(contador)
    acumulador = acumulador + contador
    contador = 2*contador + 5
    cont = cont + 1
print("Suma de los terminos: ", acumulador)    