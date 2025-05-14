"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def draw_stairs(n):
    result = ""
    for i in range(n):
        result += " " * i + "I\n"
    return result.rstrip()

if __name__ == "__main__":
    n = int(input("¿Cuántos escalones quieres?: "))
    print(draw_stairs(n))
