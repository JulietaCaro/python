divisor = 1
sumaDivisores = 0
numero = int(input("Ingrese un numero: "))
while (numero <= 0 or numero > 100) and numero != -1:
    numero = int(input("Error, ingrese un numero: "))

while numero != -1:
    divisor = 1
    sumaDivisores = 0
    while numero > divisor:
        if numero % divisor == 0:
            print("Divisor: ", divisor)
            sumaDivisores = sumaDivisores + divisor
        divisor = divisor + 1
    if sumaDivisores == numero:
        print("Es perfecto")
    if sumaDivisores < numero:
        print("Es decreciente")
    if sumaDivisores > numero:
        print("Es abundante")
    numero = int(input("Ingrese un numero: "))
    while (numero <= 0 or numero > 100) and numero != -1:
        numero = int(input("Error, ingrese un numero: "))
    
    