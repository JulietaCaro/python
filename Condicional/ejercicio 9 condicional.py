anio = int(input("Ingrese un año: "))

calculoA = anio % 19
calculoB = anio % 4
calculoC = anio % 7
calculoD = ((calculoA*19)+24)%30
calculoE = ((calculoB*2)+(calculoC*4)+(calculoD*6))%7
fechaDePascua = calculoD+calculoE+22

if fechaDePascua>31:
    fechaDePascua = fechaDePascua-31
    print("La fecha sera el ",fechaDePascua,"de abril")
else:
    print("La fecha sera el ",fechaDePascua,"de marzo")