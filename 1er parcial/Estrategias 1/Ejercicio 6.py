sumaDescuento15 = 0
contador15 = 0
sumaDescuento20 = 0
contador20 = 0
monto = int(input("Ingrese el monto de la compra: "))
while monto > 0:
    if monto > 1000 and monto <= 2000:
        descuento15 = (15*monto)//100
        sumaDescuento15 = sumaDescuento15 + descuento15
        contador15 = contador15 + 1
        print("Monto total a pagar con descuento incluido: ", monto-descuento15)
        
    if monto > 2000:
        descuento20 = (20*monto)//100
        sumaDescuento20 = sumaDescuento20 + descuento20
        contador20 = contador20 + 1
        print("Monto total a pagar con descuento incluido: ", monto - descuento20)
    
    if monto <= 1000:
        print("Total a pagar: ", monto)
        
    monto = int(input("Ingrese el monto de la compra: "))
    
if contador15 == 0 and sumaDescuento15 == 0 and contador20 == 0 and sumaDescuento20 == 0:
    print("No se ingreso nada")
else:
    print("Cantidad de compras con 15% de descuento: ", contador15)
    print("Monto total descuento del 15%: ", sumaDescuento15)
    print("Cantidad de compras con 20% de descuento: ", contador20)
    print("Monto total descuento del 20%: ", sumaDescuento20)