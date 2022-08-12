# Hacer un programa en el que ingresas un número que representa cierta cantidad de una fruta
# y divides esa cantidad por 3 chicos. Mostrar por pantalla el resultado

NUMBER_OF_KIDS = 3
total_of_fruits = int(input("Ingrese la cantidad de frutas disponible: "))
fruits_per_kid = total_of_fruits // NUMBER_OF_KIDS
remainder_of_division = total_of_fruits % NUMBER_OF_KIDS
print("A cada chico le corresonde %d fruta" % fruits_per_kid, end="")
if fruits_per_kid > 1:
    print("s")
if remainder_of_division != 0:
    print("Sobran %d frutas", remainder_of_division)
