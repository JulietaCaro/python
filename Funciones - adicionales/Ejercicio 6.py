#FUNCIONES
def signo (numero):
    numero = numero *(-1)
    return numero

#PROGRAMA PRINCIPAL
acum = 0
numero = int(input("Ingrese un numero: "))
while numero != -1:
    if numero < 0:
        numero = signo(numero)
    acum = numero + acum
    numero = int(input("Ingrese otro numero: "))
print("Suma absoluta: ", acum)
    