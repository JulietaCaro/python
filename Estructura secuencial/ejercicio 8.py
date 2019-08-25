cantidadDeDinero = int(input("Ingrese una cantidad de dinero: "))
billete100 = cantidadDeDinero//100
billete50 = (cantidadDeDinero%100)//50
billete10 = ((cantidadDeDinero%100)%50)//10
billete5 = (((cantidadDeDinero%100)%50)%10)//5
billete1 = (((cantidadDeDinero%100)%50)%10)%5
print("Billetes de 100: ", billete100)
print("Billete de 50: ", billete50)
print("Billete de 10: ", billete10)
print("Billete de 5: ", billete5)
print("Billete de 1: ", billete1)

