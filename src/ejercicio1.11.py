# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.

hours_worked = int(input("Ingrese la cantidad de horas trabajadas: "))
price_per_hour = int(input("Ingrese el coste por hora: $"))
print(f"La paga correspondiente es ${price_per_hour * hours_worked}")
