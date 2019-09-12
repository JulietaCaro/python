contador = 1
numero = int(input("Ingrese un numero: "))
while numero <= 0:
    numero = int(input("Error, reingrese el numero: "))
print(numero)
while numero != 1:
    if numero % 2 == 0:
        numero = numero // 2
        print(numero)
    else:
        numero = (numero*3) + 1
        print(numero)
    contador = contador + 1    
    
print("Cantidad de terminos obtenidos: ", contador)    