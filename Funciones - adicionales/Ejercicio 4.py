#FUNCIONES
def esMultiplo(nroA, nroB):
    if nroA % nroB == 0:
        esMultiplo = True
    else:
        esMultiplo = False
    return esMultiplo

#PROGRAMA PRINCIPAL
numero = int(input("Ingrese un numero: "))
while numero < 1:
    numero = int(input("Error, ingrese un numero positivo: "))
i = 1
contador = 0 
while i <= numero:
    if esMultiplo (numero, i) == True:
        contador = contador + 1
    i = i + 1
print("Cantidad de divisores: ", contador)
    