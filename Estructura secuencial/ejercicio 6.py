periodo = int(input("Ingrese un periodo en segundos: "))
dias = 86400
horas = 3600
minutos = 60
periodoEnDias = periodo//dias
periodoEnHoras = (periodo%dias)//horas
periodoEnMinutos = (((periodo%dias)%horas)//minutos)
periodoEnSegundos = ((periodo%dias)%horas)%minutos
print("Dias: ", periodoEnDias)
print("Horas: ", periodoEnHoras)
print("Minutos: ", periodoEnMinutos)
print("Segundos: ", periodoEnSegundos)
