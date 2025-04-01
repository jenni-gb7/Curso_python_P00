"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
Los niños beben toddy.
Los adolescentes beben coca-cola.
Los adultos jóvenes beben cerveza.
Los adultos beben whisky.
Hacer una función que reciban la edad, y devolver lo que beben.

Reglas:

Niños menores de 14 años.
Adolescentes menores de 18 años.
Jóvenes menores de 21 años.
Los adultos tienen 21 o más."""


def people_with_age_drink(age):
    if age < 14:
        return 'drink toddy'
    elif age <18:
        return 'drink coke'
    elif age < 2:
        return 'drink beer'
    else:
        return 'drink whisky'

#
if __name__ == '__main__':
    age = int(input("Ingresa tu edad:"))
    print(people_with_age_drink(age))
