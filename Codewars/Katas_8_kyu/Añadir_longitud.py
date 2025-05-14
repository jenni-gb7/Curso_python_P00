"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def add_length(str_):
    return [word + " " + str(len(word)) for word in str_.split()]

if __name__ == "__main__":
    texto = input("Escribe una frase: ")
    resultado = add_length(texto)
    print(resultado)
