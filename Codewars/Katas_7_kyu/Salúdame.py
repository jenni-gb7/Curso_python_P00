"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def greet(name):
    #Se uso el método format() para saludar el nombre
    return "Hello {}!".format(name.capitalize())

if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    print(greet(nombre))
