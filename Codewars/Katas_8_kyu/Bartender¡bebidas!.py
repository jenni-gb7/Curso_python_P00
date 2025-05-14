"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def get_drink_by_profession(param):
    newparam = param.lower()
    if newparam == "jabroni":
        return "Patron Tequila"
    elif newparam == "school counselor":
        return "Anything with Alcohol"
    elif newparam == "programmer":
        return "Hipster Craft Beer"
    elif newparam == "bike gang member":
        return "Moonshine"
    elif newparam == "politician":
        return "Your tax dollars"
    elif newparam == "rapper":
        return "Cristal"
    else:
        return "Beer"

if __name__ == "__main__":
    profesion = input("Escribe una profesión: ")
    bebida = get_drink_by_profession(profesion)
    print("Bebida sugerida:", bebida)
