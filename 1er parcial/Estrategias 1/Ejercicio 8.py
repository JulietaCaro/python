contadorApro = 0
contadorDesa = 0
contadorAplazo = 0
contadorAlumnos = 0
legajo = int(input("Ingrese el legajo del alumno: "))
while legajo < 0 and legajo != -1:
    legajo = int(input("Error, reingrese el legajo del alumno: "))
while legajo != -1:
    nota = int(input("Ingrese la nota: "))
    while nota<=0 or nota > 10:
        nota = int(input("Error, reingrese la nota: "))
    if nota >= 7:
        contadorApro = contadorApro + 1
    if nota <= 4:
        contadorDesa = contadorDesa + 1
    if nota <= 3:
        contadorAplazo = contadorAplazo + 1
    contadorAlumnos = contadorAlumnos + 1
    legajo = int(input("Ingrese el legajo del alumno: "))
    while legajo < 0 and legajo != -1:
        legajo = int(input("Error, reingrese el legajo del alumno: "))
        
if contadorApro == 0 and contadorDesa == 0 and contadorAplazo == 0 and contadorAlumnos ==0 :
    print("No se ingresaron datos")
else:
    print("Cantidad de alumnos aprobados con nota mayor o igual a 7: ", contadorApro)
    print("Cantidad de alumnos desaprobados: ", contadorDesa)
    porcentaje = (contadorAplazo*100)//contadorAlumnos
    print("Porcentaje de alumnos aplazados: ", porcentaje)