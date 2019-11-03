#FUNCIONES
import random
def buscarCodigo (listaCodigo,codigo):
    i = 0
    while i < len(listaCodigo) and listaCodigo[i] != codigo:
       i = i + 1
    if i == len(listaCodigo):
        encontrado = False
    else:
        encontrado = True
    return encontrado

def numeroRandom():
    numero = random.randint(0, 20)
    return numero

def stockMinimo(listaStock):
    cont = 0
    for i in range(0, len(listaStock)):
        if listaStock[i] < 5:
            cont = cont + 1
    return cont

def stockMaximo(listaStock):
    mayor = 0
    for i in range(0, len(listaStock)):
        if listaStock[i] > mayor:
            mayor = listaStock[i]
    return mayor

def cantidadMayorStock(listaCodigo, listaStock, mayor):
    cont = 0
    listaMayores = []
    for i in range(0, len(listaStock)):
        if listaStock[i] == mayor:
            cont = cont + 1
            listaMayores.append(listaCodigo[i])
    return cont, listaMayores

def buscarIndice(listaCodigo, codigoProducto):
    for i in range(0, len(listaCodigo)):
        if listaCodigo[i] == codigoProducto:
            indice = i
    return indice

def actualizarStock(listaStock, indice, cantidadVendida):
    if listaStock[indice] < cantidadVendida:
        print("No hay stock suficiente!")
    else:
        listaStock[indice] = listaStock[indice] - cantidadVendida
        
#PROGRAMA PRINCIPAL
listaCodigo = []
listaStock = []
codigo = int(input("Ingrese un codigo: "))
while codigo < 1000 or codigo > 9999:
    codigo = int(input("Error, reingrese el codigo: "))
while codigo != -1:
    if buscarCodigo(listaCodigo, codigo) == True:
        print("Ya existe el codigo ingresado!")
    else:
        listaCodigo.append(codigo)
        cantidadStock = numeroRandom()
        listaStock.append(cantidadStock)
    codigo = int(input("Ingrese otro codigo: "))
    while (codigo < 1000 or codigo > 9999) and codigo != -1:
        codigo = int(input("Error, reingrese el codigo: "))

for i in range(0, len(listaCodigo)):
    print("Codigo:",listaCodigo[i],"Stock:",listaStock[i])
    
minimoStock = stockMinimo(listaStock)
print("Productos con el minimo stock: ", minimoStock)

stockMayor = stockMaximo(listaStock)
maxiStock, listaMayoresCodigos = cantidadMayorStock(listaCodigo, listaStock, stockMayor)
print("Stock maximo: ", stockMayor)
print("Mayor cantidad en stock:", maxiStock,"Codigos de los productos del mayor stock:",listaMayoresCodigos)

codigoProducto = int(input("Ingrese el codigo del producto: "))
while codigoProducto < 1000 or codigoProducto > 9999:
    codigoProducto = int(input("Error, reingrese el codigo del producto"))
while codigoProducto != -1:
    if buscarCodigo(listaCodigo, codigoProducto) == True:
        cantidadVendida = int(input("Ingrese la cantidad vendida: "))
        indice = buscarIndice(listaCodigo, codigoProducto)
        actualizarStock(listaStock, indice, cantidadVendida)
    else:
        listaCodigo.append(codigoProducto)
        cantidadStock = numeroRandom()
        listaStock.append(cantidadStock)
    
    for i in range(0, len(listaCodigo)):
        print("Codigo:",listaCodigo[i],"Stock:",listaStock[i])
    
    codigoProducto = int(input("Ingrese otro codigo: "))