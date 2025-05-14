"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def remove_every_other(lista):
    return lista[::2]  # Toma uno sí, uno no (cada 2 elementos desde el índice 0)

if __name__ == "__main__":
    entrada = input("Escribe los elementos separados por comas: ").split(",")
    resultado = remove_every_other(entrada)
    print("Resultado:", resultado)
