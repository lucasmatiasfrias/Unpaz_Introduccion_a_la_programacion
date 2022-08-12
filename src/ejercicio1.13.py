# Hacer un algoritmo que nos permita introducir un número,
# luego muestre por pantalla el mensaje “Este número es par” o “este número es impar”

number = int(input("Ingrese un número: "))
if number % 2 == 0:
    print("El número %d es par" % number)
else:
    print("El número %d es impar" % number)
