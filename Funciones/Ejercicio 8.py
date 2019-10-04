#FUNCION
def mcd (a, b):
    maximo = 0
    if a > b:
        for i in range (1, a):
            if a%i==0 and b%i==0:
                maximo = i
    if a < b:
        for i in range (1, b):
            if a%i==0 and b%i==0:
                maximo = i
    if a == b:
        maximo = a
    return maximo

#PROGRAMA PRINCIPAL
num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese otro numero: "))
divisor = mcd(num1, num2)
print("Maximo comun divisor: ", divisor)
        