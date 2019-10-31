#FUNCIONES
def factorial(numero):
    i = numero
    acum = 1
    while i > 0:
        acum = acum * i
        i=i-1
    return acum

#PROGRAMA PRINCIPAL
cont = 0
numero = int(input("Ingrese un numero: "))
while numero != -1:
    if numero >= 0:
        facto = factorial(numero)
        print("El factorial es: ", facto)
    else:
        cont = cont + 1
    numero = int(input("Ingrese otro numero: "))
print("Se ingresaron",cont,"numeros negativos")

        