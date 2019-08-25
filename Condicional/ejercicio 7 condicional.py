numCliente = int(input("Ingrese el numero del cliente: "))
totalFactura = int(input("Ingrese el total de la factura: "))

print("El numero del cliente es ", numCliente)
fecha = 1

if fecha <10:
    descuento1 = totalFactura - 120
    descuento2 = totalFactura - (2*totalFactura)//100
    fecha = 15
    if descuento1>descuento2:
        print("Si abona antes de los primeros 10 dias: $", descuento1)
    else:
        print("Si abona antes de los primeros 10 dias: $", descuento2)
else:
        if  fecha<20:
            print("Si abona luego de los primeros 10 dias: $", totalFactura)
            fecha = 25
        else:
            if fecha>20:
                multa1 = totalFactura +150
                multa2 = totalFactura + (10*totalFactura)//100
                if multa1>multa2:
                    print("Si abona luego de los 20 dias: $", multa1)
                else:
                    print("Si abona luego de los 20 dias: $", multa2)
    