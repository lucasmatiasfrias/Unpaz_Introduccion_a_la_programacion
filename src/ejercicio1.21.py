# Hacer un algoritmo que se ingresa dos precios (número decimal)
# Mostrar los precios ordenado de mayor a menor

float1 = float(input("Ingrese un número decimal: "))
float2 = float(input("Ingrese otro número decimal: "))
if float1 > float2:
    print("Los números decimales ingresados en orden de mayor a menor son: %.2f %.2f" % (float1, float2))
else:
    print("Los números decimales ingresados en orden de mayor a menor son: %.2f %.2f" % (float2, float1))
