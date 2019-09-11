contadorSinDesc = 0
acumuladorSinDesc = 0
contador10 = 0
acumulador10 = 0
acumulador25 = 0
contadorVentas = 0
acumuladorCantSoli = 0
precioBase = int(input("Ingrese el precio base: "))
while precioBase <= 0:
    precioBase = int(input("Ingrese el precio base: "))
    
cantSolicitada = int(input("Ingrese la cantidad solicitada: "))
while cantSolicitada <= 0 and cantSolicitada != -1:
    cantSolicitada = int(input("Error, ingrese la cantidad solicitada: "))
while cantSolicitada != -1:
    if cantSolicitada <= 12:
        precioFinalSinDesc = precioBase * cantSolicitada
        contadorSinDesc = contadorSinDesc + 1
        acumuladorSinDesc = acumuladorSinDesc + precioFinalSinDesc
    
    if cantSolicitada >= 13 and cantSolicitada <= 100:
        precioFinal10 = (precioBase - ((10*precioBase)//100)) * cantSolicitada
        contador10 = contador10 + 1
        acumulador10 = acumulador10 + precioFinal10
    
    if cantSolicitada > 100:
        precioFinal25 = (precioBase - ((25*precioBase)//100)) * cantSolicitada
        acumulador25 = acumulador25 + precioFinal25
        
    acumuladorCantSoli = acumuladorCantSoli + cantSolicitada
    contadorVentas = contadorVentas + 1
    cantSolicitada = int(input("Ingrese la cantidad solicitada: "))
    while cantSolicitada <= 0 and cantSolicitada != -1:
        cantSolicitada = int(input("Error, ingrese la cantidad solicitada: "))
        
if contadorVentas == 0 and acumuladorCantSoli == 0 and acumulador25 == 0 and acumulador10 == 0 and contador10 == 0 and acumuladorSinDesc == 0 and contadorSinDesc == 0:    
    print("No se ingresaron datos")
else:
    valorTotalVenta = acumuladorSinDesc + acumulador10 + acumulador25
    precioPromedio = valorTotalVenta // acumuladorCantSoli
    print("Valor total de la venta: ", valorTotalVenta)
    print("Precio promedio del producto: ", precioPromedio)
    print("Cantidad de ventas realizadas: ", contadorVentas)
    print("Cantidad de ventas con 10% de descuento: ", contador10)
    print("Cantidad de ventas sin descuento aplicado: ", contadorSinDesc)
        