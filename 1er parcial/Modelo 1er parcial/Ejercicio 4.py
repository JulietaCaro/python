divisor = 1
contDivi = 0
acumDivi = 0
numero = int(input("Ingrese un numero: "))
while numero != -1:
    if numero > 0:
        divisor = 1
        contDivi = 0
        acumDivi = 0
        while divisor <= numero:
            if numero % divisor == 0:
                print("Divisor: ", divisor)
                contDivi = contDivi + 1
                acumDivi = acumDivi + divisor
            divisor = divisor + 1    
    
        print("Cantidad de divisores: ", contDivi)
        if contDivi == 2:
            print("El numero es primo")
        print("La suma de sus divisores es: ", acumDivi)
    numero = int(input("Ingrese un numero: "))