menor = 0
contador25 = 0
contador = 0
edad = int(input("Ingrese la edad: "))
while (edad < 0 or edad >100) and edad != -1:
    edad = int(input("Error, reingrese la edad: "))
while edad != -1:
    if edad > 25:
        contador25 = contador25 + 1
    if contador == 0 or edad < menor:
        menor = edad
    
    contador = contador + 1
    edad = int(input("Ingrese la edad: "))
porcentaje = (contador25 * 100) / contador
print("Cantidad de personas que asistieron: ", contador)
print("Porcentaje de personas mayores a 25: ", porcentaje)
print("Edad de la persona mas joven: ", menor)