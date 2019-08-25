binario = int(input("Ingrese un numero en binario: "))
cuartaCifra = (binario%10)*2**0
binario = binario // 10
terceraCifra = (binario%10)*2**1
binario = binario // 10
segundaCifra = (binario%10)*2**2
binario = binario // 10
primeraCifra = (binario%10)*2**3
print("El numero en decimal es ", primeraCifra+segundaCifra+terceraCifra+cuartaCifra)
 

