base = int(input("Ingrese la base de un triangulo: "))
#altura = int(input("Ingrese la altura de un triangulo: "))
if base<0:
    print("La base ingresada es negativa")
else:
    altura = int(input("Ingrese la altura de un triangulo: "))
    if altura<0:
        print("La altura ingresada es negativa")
    else:
        print("La superficie es: ", (base*altura)//2)
    