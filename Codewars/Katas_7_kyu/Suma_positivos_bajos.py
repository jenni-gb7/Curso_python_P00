"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

if __name__ == "__main__":
    entrada = input("Ingresa al menos 4 números positivos separados por comas: ")
    partes = entrada.split(",")
    numeros = []
    for p in partes:
        numeros.append(int(p))

    resultado = sum_two_smallest_numbers(numeros)
    print("La suma de los dos números más pequeños es:", resultado)
