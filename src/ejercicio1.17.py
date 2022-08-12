# Hacer un algoritmo que ingresa 2 letras, mostrarlas por pantalla ordenadas alfabéticamente.

letter1 = input("Ingrese una letra: ")
letter2 = input("Ingrese otra letra: ")
if len(letter1) == len(letter2) == 1:
    if letter1 < letter2:
        print("Las letras ingresadas en orden alfabetico son: %c %c" % (letter1, letter2))
    else:
        print("Las letras ingresadas en orden alfabetico son: %c %c" % (letter2, letter1))
