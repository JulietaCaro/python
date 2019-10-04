#FUNCION
def multiplo(a, b):
    if a%b==0:
        numero = True
    else:
        numero = False
    return numero

#PROGRAMA PRINCIPAL
numero = int(input("Ingrese un numero: "))
segundoNum = int(input("Ingrese otro numero: "))
num = multiplo(numero, segundoNum)
print(num)