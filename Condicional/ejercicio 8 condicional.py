anio = int(input("Ingrese un año: "))

if anio%4==0 and anio%400==0:
    print("El anio", anio, "es bisiesto")
else:
    #if anio%4==0 and anio%100==0:
    print("El anio", anio,"no es bisiesto")
