# Hacer un algoritmo que se ingresa un precio (número decimal) y le calcula un incremento de 10%
# Mostrar por pantalla el resultado

INCREASE = .10
final_price = float(input("Ingrese el precio (número decimal): $"))
final_price += final_price * INCREASE
print("El precio con un incremento del %%%d es: $%.2f" % (INCREASE * 100, final_price))
