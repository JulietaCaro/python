contPos = 0
resultado = 0
contDig = 0
numero = int(input("Ingrese un numero: "))
while numero != -1:
    if numero < 0:
        numPositivo = numero * (-1)
        print("Nro positivo: ", numPositivo)
        contPos = contPos + 1
        resultado = 0
        contDig = 0
        while numPositivo != 0:
            digito = numPositivo % 10
            resultado = resultado + digito
            numPositivo = numPositivo // 10
            contDig = contDig + 1
    
        print("Cantidad de digitos: ", contDig)
        print("Suma de los digitos: ", resultado)
    numero = int(input("Ingrese un numero: "))
print("Cantidad de numeros convertidos a positivos: ", contPos)    