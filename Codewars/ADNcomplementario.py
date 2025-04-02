"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
En las cadenas de ADN, los símbolos "A" y "T" son complementos entre sí, como "C" y "G". Su función recibe un lado del ADN (cadena, a excepción de Haskell); Es necesario devolver el otro lado complementario.
Ejemplo: (entrada --> salida)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"""

#3
def DNA_strand(dna):

    texto_convertido = ""
    for letra in dna:
        if letra == "A":
            texto_convertido += "T"
        elif letra == "T":
            texto_convertido += "A"
        elif letra == "C":
            texto_convertido += "G"
        elif letra == "G":
            texto_convertido += "C"
        else:
            texto_convertido += letra  # Dejar el carácter sin cambios.
    return texto_convertido




if __name__ == '__main__':
    dna = str( input("Ingresa la cadena:"))
    texto_convertido = DNA_strand(dna)
    print(texto_convertido)