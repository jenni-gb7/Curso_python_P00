"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.

Descripción del programa:
Este programa recibe el nombre de un peleador y devuelve una frase icónica asociada a él.
Si el peleador ingresado es "George Saint Pierre", devuelve:
    "I am not impressed by your performance."
Para cualquier otro peleador, devuelve:
    "I'd like to take this chance to apologize.. To absolutely NOBODY!"
"""

def quote(fighter: str) -> str:
    """
    Función que devuelve una frase dependiendo del peleador ingresado.
    :Param: fighter (str): Nombre del peleador.
    Return: str: Frase icónica del peleador.
    """
    newfighter = fighter.lower()  # Convierte la cadena a minúsculas para hacer la comparación insensible a mayúsculas

    # Verifica si el peleador es George Saint Pierre
    if newfighter == 'george saint pierre':
        return "I am not impressed by your performance."
    else:
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"

if __name__ == '__main__':
    # Solicita el nombre del peleador al usuario
    fighter = str(input("Ingresa el nombre del peleador: "))

    # Muestra la frase correspondiente
    print(quote(fighter))
