# Hacer un algoritmo que pida un número entero y determine si es múltiplo de 5. Muestra un mensaje por pantalla.

MULTIPLE = 5
number = int(input("Ingrese un número: "))
if number % MULTIPLE == 0:
    print("El número %d es múltiplo de %d" % (number, MULTIPLE))
