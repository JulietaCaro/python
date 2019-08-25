sueldoBasico = int(input("Ingrese el sueldo basico: "))
antiguedad = int(input("Ingrese la antigüedad: "))
estadoCivil = input("ingrese el estado civil 's' o 'c': ")

print("Sueldo basico: ", sueldoBasico)
print("Antigüedad: ", antiguedad)

if estadoCivil != 's' and estadoCivil != 'c':
    print("Letra incorrecta")

if estadoCivil == 's':
    print("Estado civil: Soltero")
    soltero = (sueldoBasico*5/100)*antiguedad
    sueldoBruto = soltero + sueldoBasico
    print("Sueldo bruto: ", sueldoBruto)
    jubilacion = (sueldoBruto*11/100)
    print("Jubilacion: ", jubilacion)
    obraSocial = (sueldoBruto*3/100)
    print("Obra social: ", obraSocial)
    sindicato = (sueldoBruto*3/100)
    print("Sindicato: ", sindicato)
    descuentos = jubilacion + obraSocial + sindicato
    sueldoNeto = sueldoBruto - descuentos
    print("Sueldo neto: ", sueldoNeto)
    
else:
    if estadoCivil == 'c':
        print("Estado civil: Casado")
        casado = (sueldoBasico*7/100)*antiguedad
        sueldoBruto = casado + sueldoBasico
        print("Sueldo bruto: ", sueldoBruto)
        jubilacion = (sueldoBruto*11/100)
        print("Jubilacion: ", jubilacion)
        obraSocial = (sueldoBruto*3/100)
        print("Obra social: ", obraSocial)
        sindicato = (sueldoBruto*3/100)
        print("Sindicato: ", sindicato)
        descuentos = jubilacion + obraSocial + sindicato
        sueldoNeto = sueldoBruto - descuentos
        print("Sueldo neto: ", sueldoNeto)
        



