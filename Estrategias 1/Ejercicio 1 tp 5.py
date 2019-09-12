contador = 1
cont = 0
error = 0
semanas = int(input("Ingrese la cantidad de semanas: "))
while semanas < 0:
    semanas = int(input("Error, reingrese la cantidad de semanas: "))

while cont<semanas:
    error = 2**contador
    contador = contador + 2
    cont = cont + 1

print("Errores a cometer: ", error)    