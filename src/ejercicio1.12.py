# Hacer un algoritmo que nos permita introducir un número,
# luego muestre por pantalla el mensaje “Este número es positivo” o “Este número es negativo”

number = int(input("Ingrese un número: "))
if number > 0:
    print("El número %d es positivo" % number)
elif number < 0:
    print("El número %d es negativo" % number)
