medidaEnMetros = int(input("Ingrese una medida en metros: "))
medidaEnCm = medidaEnMetros*100
medidaEnPulgada = medidaEnCm/2.54
medidaEnPie = medidaEnPulgada/12
medidaEnYarda = medidaEnPie/3
print("Medida expresada en centimetros: ", medidaEnCm)
print("Medida expresada en pulgadas: ", medidaEnPulgada)
print("Medida expresada en pies: ", medidaEnPie)
print("Medida expresada en yardas: ", medidaEnYarda)