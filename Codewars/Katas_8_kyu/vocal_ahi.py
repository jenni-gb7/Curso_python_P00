"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""


def is_vow(inp):
    nueva = []
    for num in inp:
        if num == 97:
            nueva.append('a')
        elif num == 101:
            nueva.append('e')
        elif num == 105:
            nueva.append('i')
        elif num == 111:
            nueva.append('o')
        elif num == 117:
            nueva.append('u')
        else:
            nueva.append(num)
    return nueva


if __name__ == "__main__":
    entrada = input("Escribe los números separados por comas: ")
    partes = entrada.split(",")
    inp = []
    for p in partes:
        inp.append(int(p))

    resultado = is_vow(inp)
    print(resultado)

