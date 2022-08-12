#Hacer un programa en el que se ingresa precio y calcula el precio final con el iva (21%).
#Mostrar el resultado por pantalla

IVA = .21
price = int(input("Ingrese el precio: $"))
print("El precio más IVA es: $%.2f" % (price + price * IVA))
