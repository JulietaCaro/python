acumMenos10 = 0
contMenos10 = 0
contMas10 = 0
acumMas10 = 0
contador = 0
mayor = 0
peso = int(input("Ingrese el peso del cajon: "))
while peso < 0:
    peso = int(input("Error, reingrese el peso del cajon: "))

while peso != 0:
    if peso < 10:
        acumMenos10 = acumMenos10 + peso
        contMenos10 = contMenos10 + 1
    if peso >= 10:
        acumMas10 = acumMas10 + peso
        contMas10 = contMas10 + 1
        
    if contador == 0 or peso > mayor:
        mayor = peso
        
    contador = contador + 1
    peso = int(input("Ingrese el peso del cajon: "))
if contador != 0:
    print("Cantidad de cajones -10 kg: ", contMenos10)
    print("Suma total cajones -10 kg: ", acumMenos10)
    print("Cantidad de cajones + 10 kg: ", contMas10)
    print("Suma total cajones + 10 kg: ", acumMas10)
else:
    print("No se ingreso nada")
        