cont = 0
termino = int(input("Ingrese los terminos: "))
while termino <= 0:
    termino = int(input("Error, reingrese los terminos: "))

while cont<(termino//2):
    serie2 = 2 ** cont
    serie3 = 3 ** cont
    print(serie2)
    print(serie3)
    cont = cont + 1