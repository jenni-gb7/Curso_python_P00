"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
Reemplace todas las vocales por signos de exclamación en la oración. es vocal.aeiouAEIOU
"Hi!" --> "H!!"
"!Hi! Hi!" --> "!H!! H!!"
"aeiou" --> "!!!!!"
"ABCDE" --> "!BCD!"
"""

def replace_exclamation(us):
    st = ""  # Cadena vacía para almacenar el resultado
    for Letra in us:
         # Reemplazar vocales minúsculas y mayúsculas.
        if Letra == 'a' or Letra == 'A':
            st += '!'
        elif Letra == 'e' or Letra == 'E':
            st += '!'
        elif Letra == 'i' or Letra == 'I':
            st += '!'
        elif Letra == 'o' or Letra == 'O':
            st += '!'
        elif Letra == 'u' or Letra == 'U':
            st += '!'
        else:
            st += Letra  # Dejar el carácter sin cambios.
    return st

if __name__ == '__main__':
    us = (input("Ingresa la cadena:"))
    st = replace_exclamation(us)
    print(st)