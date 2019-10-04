#FUNCION
def extraerDigito(a, b):
    contD = 0
    num = a
    while num != 0:
        digitos = num % 10
        contD = contD + 1
        num = num // 10
    if contD < b:
        division = -1
    else:
        for i in range (0, (b+1)):
            division = a % 10
            a = a // 10
    return division

#PROGRAMA PRINCIPAL
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
cifra = extraerDigito(num1, num2)
print(cifra)