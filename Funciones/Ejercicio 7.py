def factorial (a):
    cont = 1
    for i in range(1, (a+1)):
        cont = i * cont
    return cont

#PROGRAMA PRINCIPAL
num = int(input("Ingrese un numero: "))
fact = factorial(num)
print("Factorial: ", fact)