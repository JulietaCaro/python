#FUNCION
def fibonacci (a):
    acum = 1
    for i in range(1, a):
        acum = acum + i
    return acum

def fibonacci2(a, b):
    acum1 = 1
    acum2 = 1
    for i in range(1, b):
        acum1 = acum1 + i
        if a >= i:
            acum2 = acum1 + i
    return acum2

#PROGRAMA PRINCIPAL
nro1 = int(input("Ingrese un numero: "))
nro2 = int(input("Ingrese otro numero: "))
sucesion = fibonacci2(nro1, nro2)
print("Suma: ", sucesion)