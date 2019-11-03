#FUNCIONES
def buscarSocio(listaUrgencia, listaTurno, codigoABuscar):
    ordenUrgencia = []
    ordenTurno = []
    contUrgen = 0
    contTurno = 0
    for i in range(0, len(listaUrgencia)):
        if listaUrgencia[i] == codigoABuscar:
            contUrgen = contUrgen + 1
            ordenUrgencia.append(i+1)
            
    for i in range(0, len(listaTurno)):
        if listaTurno[i] == codigoABuscar:
            contTurno = contTurno + 1
            ordenTurno.append(i+1)
    return contUrgen, ordenUrgencia, contTurno, ordenTurno                        

#PROGRAMA PRINCIPAL
listaUrgencia = []
listaTurno = []
codigoSocio = int(input("Ingrese el codigo del socio: "))
while (codigoSocio < 1000 or codigoSocio > 9999) and codigoSocio != -1:
    codigoSocio = int(input("Error, reingrese el codigo del socio: "))

while codigoSocio != -1:
    porqueViene = int(input("Ingrese 1 por urgencia 2 por turno: "))
    while porqueViene != 1 and porqueViene != 2:
        porqueViene = int(input("Error, reingrese 1 por urgencia 2 por turno: "))
    
    if porqueViene == 1:
        listaUrgencia.append(codigoSocio)
    
    else:
        listaTurno.append(codigoSocio)
    
    codigoSocio = int(input("Ingrese el codigo del socio: "))
    while (codigoSocio < 1000 or codigoSocio > 9999) and codigoSocio != -1:
        codigoSocio = int(input("Error, reingrese el codigo del socio: "))
    
print("SOCIOS ATENDIDOS POR URGENCIA")
print(listaUrgencia)
print("")
print("SOCIOS ATENDIDOS POR TURNO")
print(listaTurno)
codigoBuscar = int(input("Ingrese el codigo a buscar: "))
while codigoBuscar<1000 or codigoBuscar>9999:
    codigoBuscar = int(input("Error, reingrese el codigo a buscar: "))
urgenciaCont, ordenUrgen, turnoCont, ordenTurno = buscarSocio(listaUrgencia, listaTurno, codigoBuscar)
if urgenciaCont == 0 and turnoCont == 0:
    print("El codigo",codigoBuscar,"no se atendió")
if turnoCont == 0:
    print("El socio se atendio por urgencia",urgenciaCont,"veces en el orden",ordenUrgen)
else:
    if urgenciaCont == 0:
        print("El socio se atendio por turno",turnoCont,"veces en el orden",ordenTurno)
    else:
        print("El socio se atendio por urgencia",urgenciaCont,"veces en el orden",ordenUrgen,"y",turnoCont,"veces en el orden",ordenTurno)