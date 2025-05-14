"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def words_to_marks(s):
    total = 0
    for letra in s:
        valor = ord(letra) - 96  # 'a' = 97 en ASCII, así que restamos 96
        total += valor
    return total

if __name__ == "__main__":
    palabra = input("Escribe una palabra en minúsculas: ")
    resultado = words_to_marks(palabra)
    print("El valor de la palabra es:", resultado)
