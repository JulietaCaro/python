#FUNCIONES
def mayorPromedio(listaPromocionados, legajoPromocionados, listaNota1, listaNota2):
    mayorProm = 0
    for i in range(0, len(listaPromocionados)):
        if listaPromocionados[i] > mayorProm:
            mayorProm = listaPromocionados[i]
            indice = i
    nota1 = listaNota1[indice]
    nota2 = listaNota2[indice]
    legajo = legajoPromocionados[indice]
    
    return mayorProm, legajo, nota1, nota2

def validar(valorMinimo, valorMaximo, mensaje):
    valor = int(input(mensaje))
    while (valor < valorMinimo or valor > valorMaximo) and valor != -1:
        valor = int(input(mensaje))
    return valor

#PROGRAMA PRINCIPAL
listaPromocionados = []
legajosPromocionados = []
listaNota1 = []
listaNota2 = []
leg=validar(0, 1000000, "Ingrese el legajo del alumno: ")
while leg!=-1:
    nota1 = validar(0,10,"Ingrese la primera nota: ")
    nota2 = validar(0,10,"Ingrese la segunda nota: ")
    if nota1 >= 7 and nota2 >= 7:
        print("El alumno promocionó! ☺")
        promedio = (nota1 + nota2) // 2
        listaPromocionados.append(promedio)
        legajosPromocionados.append(leg)
        listaNota1.append(nota1)
        listaNota2.append(nota2)
        
    if nota1 < 4 and nota2 < 4:
        print("El alumno debe recuperar los dos parciales")
    
    if (nota1 >= 4 and nota2 < 7) or (nota1 >= 4 and nota2 < 7):
        print("El alumno debe rendir final")
    
    if nota1 < 7 and nota2 >= 4:
        print("El alumno debe recuperar el primer parcial")
        
    if nota1 >= 4 and nota2 < 4:
        print("El alumno debe recuperar el segundo parcial")
    
    leg=validar(0, 1000000, "Ingrese el legajo del alumno: ")
    

if len(listaPromocionados) == 0:
    print("No promocionó ningun alumno!")
else:
    mayorProm, legajoMayor, nota1Mayor, nota2Mayor = mayorPromedio(listaPromocionados, legajosPromocionados, listaNota1, listaNota2)
    print("Mayor promedio:",mayorProm,"Legajo:",legajoMayor,"Nota 1:",nota1Mayor,"Nota 2:",nota2Mayor)