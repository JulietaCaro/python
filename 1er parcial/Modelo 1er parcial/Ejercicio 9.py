contador = 0
importe = int(input("Ingrese el importe de la compra: "))
while importe < 0:
    importe = int(input("Error, reingrese el importe de la compra: "))
while importe != 0:
    if importe < 3000:
        puntosSinAdicion = importe // 3
        print("Puntos conseguidos: ", puntosSinAdicion)
    if importe >= 3000:
        puntosConAdicion = (importe // 3) + 10
        print("Puntos conseguidos: ", puntosConAdicion)
    if contador == 0 or importe > mayor:
        mayor = importe
        cont = contador + 1

    contador = contador + 1
    importe = int(input("Ingrese el importe de la compra: "))

print("Mayor compra realizada: ", mayor)
print("La mayor compra se ingresó en la orden: ", cont)
