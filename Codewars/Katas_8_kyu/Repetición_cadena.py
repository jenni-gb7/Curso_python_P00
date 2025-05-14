"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def repeat_str(repeat, string):
    return string * repeat

if __name__ == "__main__":
    repeat = int(input("¿Cuántas veces quieres repetir?: "))
    string = input("¿Qué texto quieres repetir?: ")
    resultado = repeat_str(repeat, string)
    print("Resultado:", resultado)
