"""
Ingresar dos números e informar la suma, multiplicación, división y resta de ellos.
Si el segundo número es cero la división debe mostrar “No puede realizarse la operación”
"""

number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))
print("La suma de %d + %d es : %d" % (number1, number2, number1 + number2))
print("La multiplicación de %d * %d es : %d" % (number1, number2, number1 * number2))
print("La resta de %d - %d es : %d" % (number1, number2, number1 - number2))
if number2 == 0:
    print("No puede realizarse la operación")
else:
    print("La división de %d / %d es : %.2f" % (number1, number2, number1 / number2))
