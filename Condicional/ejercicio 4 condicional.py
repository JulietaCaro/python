numeroA = int(input("Ingrese un numero: "))
numeroB = int(input("Ingrese otro numero: "))
if numeroA%numeroB==0:
    print("El numero ",numeroA,"es multiplo del numero ",numeroB)
else:
    if numeroB%numeroA==0:
        print("El numero ",numeroB,"es multiplo del numero ",numeroA)
  
    