# Hacer un algoritmo que ingresé un número decimal,
# súmale 15 y dividí por 2 mostrar el resultado por pantalla en formato decimal

TO_ADD = 15
TO_DIVIDE = 2
number = float(input("Ingrese un número decimal: "))
print("Resultado de (%.2f + %d) / %d = %.2f" % (number, TO_ADD, TO_DIVIDE, (number + TO_ADD) / TO_DIVIDE))
