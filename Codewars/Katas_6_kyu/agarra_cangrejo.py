"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def grabscrab(said, possible_words):
    result = []
    for word in possible_words:
        if sorted(word) == sorted(said):
            result.append(word)
    return result

if __name__ == "__main__":
    said = input("Escribe las letras revoltijas: ")
    possible_words = input("Escribe las palabras posibles separadas por comas: ").split(",")
    print(grabscrab(said, possible_words))
