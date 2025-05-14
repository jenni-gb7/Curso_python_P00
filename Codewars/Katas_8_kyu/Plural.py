"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def plural(n):
    return n != 1

if __name__ == "__main__":
    numero = float(input("Escribe un número: "))
    print("¿Se debe usar plural?", plural(numero))
