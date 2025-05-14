"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def string_clean(s):
    """
    Esta función elimina todos los números de la cadena s
    y mantiene todo lo demás igual.
    """
    resultado = ''
    for caracter in s:
        if not caracter.isdigit():
            resultado += caracter
    return resultado

if __name__ == "__main__":
    texto = input("Escribe el texto con números: ")
    limpio = string_clean(texto)
    print("Texto limpio:", limpio)
