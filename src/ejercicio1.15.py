# Hacer un algoritmo que ingrese dos números y determinar si alguno de los dos números es divisible por 3.

MULTIPLE = 5
number1 = int(input("Ingrese un número: "))
number2 = int(input("Ingrese otro número: "))
if number1 % MULTIPLE == 0 or number2 % MULTIPLE == 0:
    print("Alguno de los números ingresados es divisible por %d" % MULTIPLE)
