#FUNCION
def digitoCentral(a):
    contD = 0
    num = a
    while num!=0:
        digito = num % 10
        contD = contD + 1
        num = num // 10
    if contD % 2 != 0:
        contD = (contD//2)+1
        for i in range (0, contD):
            digito = a % 10
            a = a//10
    else:
        digito = -1
    return digito
#PROGRAMA PRINCIPAL
nro = int(input("Ingrese un numero: "))
central = digitoCentral(nro)
print(central)