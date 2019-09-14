contador = 0
contPrimer = 0
coordenadas = int(input("Ingrese las coordenadas a escribir: "))
while coordenadas < 0:
    coordenadas = int(input("Ingrese las coordenadas a escribir: "))
while contador < coordenadas:
    x = int(input("Ingrese el valor de x: "))
    y = int(input("Ingrese el valor de y: "))
    
    if x > 0 and y > 0:
        print(x,",",y,"Pertece al cuadrante I")
        contPrimer = contPrimer + 1
        
    if x > 0 and y < 0:
        print(x,",",y,"Pertece al cuadrante IV")
    
    if x < 0 and y > 0:
        print(x,",",y,"Pertece al cuadrante II")
    
    if x < 0 and y < 0:
        print(x,",",y,"Pertece al cuadrante III")
    
    if x == 0 or y == 0:
        print(x,",",y,"No pertece a ningun cuadrante")
    contador = contador + 1