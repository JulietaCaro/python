#FUNCION
def signo (n):
    if n>0:
        num = 1
    else:
        if n < 0:
            num = -1
        else:
            num = 0
    return num

#PROGRAMA PRINCIPAL
numero = int(input("Ingrese un numero: "))
nro = signo(numero)
print(nro)