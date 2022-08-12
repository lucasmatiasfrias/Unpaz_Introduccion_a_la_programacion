# Hacer un algoritmo que se ingresa el tiempo registrado de dos autos que recorrieron una pista de 10 kilómetros.
# El tiempo se guardó como número decimal.
# Mostrar por pantalla cuál auto fue más rápido y a qué velocidad hizo el recorrido

DISTANCE_IN_KILOMETERS = 10
MINUTES_PER_HOUR = 60
car1_time = float(input("Ingrese el tiempo del primer auto (en minutos): "))
car2_time = float(input("Ingrese el tiempo del segundo auto (en minutos): "))
car1_speed = DISTANCE_IN_KILOMETERS / car1_time * MINUTES_PER_HOUR
car2_speed = DISTANCE_IN_KILOMETERS / car2_time * MINUTES_PER_HOUR
if car1_speed > car2_speed:
    print("El primer auto fue el mas rápido a una velocidad de %.2f km/h" % car1_speed)
else:
    print("El segundo auto fue el mas rápido a una velocidad de %.2f km/h" % car2_speed)
