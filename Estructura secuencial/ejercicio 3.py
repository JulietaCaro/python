verde = int(input("Ingrese la cantidad de cortinas verdes: "))
blanco = int(input("Ingrese la cantidad de cortinas blancas: "))
azul = int(input("Ingrese la cantidad de cortinas azules: "))
sumaCortinas = verde + blanco +azul
porcVerde = (verde*100)//sumaCortinas
porcBlanco = (blanco*100)//sumaCortinas
porcAzul = (azul*100)//sumaCortinas

print("El porcentaje de verde es: ",porcVerde, "%")
print("El porcentaje de blanco es: ",porcBlanco, "%")
print("El porcentaje de azul es: ",porcAzul, "%")
