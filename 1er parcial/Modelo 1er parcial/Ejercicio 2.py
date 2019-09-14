contador = 1
acumulador = 0
numeroN = int(input("Ingrese un numero positivo: "))
while numeroN < 0:
    numeroN = int(input("Error, ingrese un numero positivo: "))
while contador <= numeroN:
    print(contador)
    acumulador = acumulador + contador
    contador = contador + 2
print("Suma de los numero impares: ", acumulador)    