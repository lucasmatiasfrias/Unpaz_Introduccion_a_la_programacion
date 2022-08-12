# Hacer un programa que ingresa un precio y calcula un descuento del 9%. Mostrar por pantalla el resultado

DISCOUNT = .09
price = int(input("Ingrese el precio: $"))
print("El precio con un descuento del %%%d es: $%.2f" % (DISCOUNT * 100, price - price * DISCOUNT))
