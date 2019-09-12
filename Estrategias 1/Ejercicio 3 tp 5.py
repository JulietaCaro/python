cont = 1
terminos = int(input("Ingrese la cantidad de terminos: "))
while terminos <= 0:
    terminos = int(input("Error, reingrese la cantidad de terminos: "))
    
while cont <= terminos:
    sumatoria = cont * (-1) ** cont
    print(sumatoria)
    cont = cont + 1
    
    