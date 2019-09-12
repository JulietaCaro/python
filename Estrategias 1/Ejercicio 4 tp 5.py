cont = 0
acum = 1
termino = int(input("Ingrese el tope: "))
while termino <= 0:
    termino = int(input("Error, reingrese el tope: "))

while acum + cont< termino:    
    acum = acum + cont
    print(acum)
    cont = cont + 1