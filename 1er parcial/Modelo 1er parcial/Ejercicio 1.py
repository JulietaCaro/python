contador = 0
contador2 = 0
puntosAIngresar = int(input("Ingrese la cantidad de puntos a ingresar: "))
while puntosAIngresar < 0:
    puntosAIngresar = int(input("Error, reingrese la cantidad de puntos a ingresar: "))
while contador< puntosAIngresar:
    x = int(input("Ingrese el valor de x: "))
    y = int(input("Ingrese el valor de y: "))
    
    if x > 0 and y > 0:
        print(x,",",y, "Pertenece al cuadrante I")
        calculo = x**2 + x*3 + 5
        print("Resultado del calculo: ", calculo)
    if x < 0 and y > 0:
        print(x,",",y, "Pertenece al cuadante II")
        contador2 = contador2 + 1
    if x < 0 and y < 0:
        print(x,",",y, "Pertenece al cuadrante III")
    if x > 0 and y < 0:
        print(x,",",y, "Pertenece al cuadrante IV")
    
    if x == 0 or y == 0:
        print(x,",",y,"No pertenece a ningun cuadrante")
        
    contador = contador + 1

if contador2 == 0 and contador== 0:
    print("No se ingresaron datos")
else:    
    print("Puntos del cuadrante II: ", contador2)
    