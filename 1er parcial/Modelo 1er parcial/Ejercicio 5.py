contador = 1
numero = int(input("Ingrese un numero positivo: "))
while numero <= 0:
    numero = int(input("Error, ingrese un numero positivo: "))
while contador < numero:
    if (contador * (contador + 1)) == numero:
        print(numero,"es oblongo")
        print("Los numeros son",contador,"y",contador+1)
    contador = contador + 1
        