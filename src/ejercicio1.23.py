# Hacer un algoritmo que se ingresa tres números. Mostrar por pantalla si están ordenados de menor a mayor

number1 = int(input("Ingrese un número: "))
number2 = int(input("Ingrese un número: "))
number3 = int(input("Ingrese un número: "))
if number1 < number2 < number3:
    print("Los números ingresados estan ordenados de menor a mayor")
else:
    print("Los números ingresados NO estan ordenados de menor a mayor")
