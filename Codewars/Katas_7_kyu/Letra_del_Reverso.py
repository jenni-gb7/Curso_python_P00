"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def reverse_letter(st):
    #
    # Letras alfabéticas y luego invertir la cadena
    return ''.join([c for c in st if c.isalpha()])[::-1]

if __name__ == "__main__":
    entrada = input("Escribe una cadena: ")
    resultado = reverse_letter(entrada)
    print("Resultado:", resultado)
