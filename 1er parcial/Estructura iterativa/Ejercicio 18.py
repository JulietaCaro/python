resultado = 0
numero = int(input("Ingrese un numero positivo (-1 para terminar): "))

while numero <= 0 and numero != -1: #validar el dato
    numero = int(input("Error, ingrese un numero positivo: "))
#el dato ya esta validado, ahora se suma    
while numero != -1: 
    #volver a inicializar el result ya que queda con el dato anterior
    resultado = 0 
    #separando en digitos y sumando
    while numero != 0: 
        digito= numero % 10
        resultado = resultado + digito
        numero = numero // 10
    print("Suma: ", resultado)
    #pido otro numero
    numero = int(input("Ingrese un numero positivo (-1 para terminar): "))
    while numero <= 0 and numero != -1:
        numero = int(input("Error, ingrese un numero positivo: "))