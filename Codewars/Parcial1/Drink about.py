"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.

Descripción del programa:
Este programa recibe la edad de una persona y devuelve la bebida que le corresponde según su grupo de edad.

Reglas:
- Niños menores de 14 años beben toddy.
- Adolescentes menores de 18 años beben coca-cola.
- Jóvenes menores de 21 años beben cerveza.
- Adultos de 21 años o más beben whisky.
"""

def people_with_age_drink(age: int) -> str:
    """
    Determina la bebida correspondiente según la edad.
    Parámetros: age (int): La edad de la persona.
    Retorna: str: La bebida recomendada según la edad.
    """
    if age < 14:
        return 'drink toddy'
    elif age < 18:
        return 'drink coke'
    elif age < 21:  # Se corrigió el error en la condición (antes decía `< 2` en lugar de `< 21`)
        return 'drink beer'
    else:
        return 'drink whisky'

if __name__ == '__main__':
    # Solicita la edad del usuario
    age = int(input("Ingresa tu edad: "))

    # Muestra la bebida correspondiente
    print(people_with_age_drink(age))
