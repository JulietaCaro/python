contadorTotalVentas = 0
contador10 = 0
contadorSinDes = 0
cantSoli = int(input("Ingrese la cantidad solicitada: "))
while cantSoli <= 0 and cantSoli != -1:
    cantSoli = int(input("Error, reingrese la cantidad solicitada: "))
while cantSoli != -1:
    precioBase = int(input("Ingrese el precio base: "))
    while precioBase <= 0:
        precioBase = int(input("Error, reingrese el precio base: "))
    if cantSoli <= 12:
        precioFinalSinDesc = cantSoli * precioBase
        print("Precio final: ", precioFinalSinDesc)
        promedio = precioFinalSinDesc / cantSoli
        print("Promedio por unidad: %.2f" %promedio)
        contadorSinDes = contadorSinDes + 1
    
    if cantSoli >= 13 and cantSoli <= 100:
        precioFinal10 = precioBase * 12 + (precioBase - (10*precioBase)//100) * (cantSoli - 12)
        print("Precio final: ", precioFinal10)
        promedio = precioFinal10 / cantSoli
        print("Promedio por unidad: %.2f" %promedio)
        contador10 = contador10 + 1
    
    if cantSoli > 100:
        precioFinal25= precioBase*12 + (precioBase - (10*precioBase)//100) * 88 + (precioBase - (25*precioBase)//100) * (cantSoli - 100)
        print("Precio final: ", precioFinal25)
        promedio = precioFinal25 / cantSoli
        print("Promedio por unidad: %.2f" %promedio)
    
    contadorTotalVentas = contadorTotalVentas + 1
    cantSoli = int(input("Ingrese la cantidad solicitada: "))

if contadorTotalVentas == 0:
    print("No se ingresaron datos")
else:
    print("Cantidad de ventas realizadas: ", contadorTotalVentas)
    print("Cantidad de ventas con 10% de descuento", contador10)
    print("Cantidad de ventas sin descuento: ",contadorSinDes)