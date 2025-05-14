"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst

if __name__ == "__main__":
    entrada = input("Escribe los animales separados por comas: ").split(",")
    resultado = list_animals(entrada)
    print(resultado)