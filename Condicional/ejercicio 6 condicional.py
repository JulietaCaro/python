paginas = int(input("Ingrese la cantidad de paginas: "))
if paginas<300:
    costo1 = 125 + (paginas*2.20)
    print("El costo es de ", costo1)
else:
    if paginas>300 and paginas<600:
        #costo2 = 125 + (paginas * 80)
        costo2 =int( 125 + 80 + (paginas * 2.20))
        print("El costo es de ", costo2)
    else:
        if paginas>600:
            #costo3 = 125 + paginas * 136
            costo3 = int(125 + 136 + (paginas * 2.20))
            print("El costo es de ", costo3)