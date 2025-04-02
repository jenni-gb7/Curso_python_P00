"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.

Descripción del programa:
En las cadenas de ADN, los símbolos "A" y "T" son complementos entre sí, al igual que "C" y "G".
Esta función recibe una cadena de ADN y devuelve su complemento correspondiente.

Ejemplo:
Entrada: "ATTGC"
Salida:  "TAACG"
"""

def DNA_strand(dna):
    """
    Función que recibe una cadena de ADN y devuelve su complemento.
    Param:dna (str): La cadena de ADN de entrada.
    Return:str: La cadena complementaria de ADN.
    """
    texto_convertido = ""  # Variable para almacenar la cadena resultante

    for letra in dna:
        # Se verifica cada letra y se asigna su complemento
        if letra == "A":
            texto_convertido += "T"
        elif letra == "T":
            texto_convertido += "A"
        elif letra == "C":
            texto_convertido += "G"
        elif letra == "G":
            texto_convertido += "C"
        else:
            texto_convertido += letra  # Si hay un carácter desconocido, se deja igual

    return texto_convertido


if __name__ == '__main__':
    # Solicita al usuario una cadena de ADN
    dna = str(input("Ingresa la cadena de ADN: "))

    # Genera la cadena complementaria
    texto_convertido = DNA_strand(dna)

    # Imprime el resultado
    print("Cadena complementaria:", texto_convertido)
