"""
Jennifer Marlene Gutiérrez Beteta
10 de Abril de 2025.

Descripción del programa:
Su trabajo consiste en escribir una sencilla función de validación de contraseñas, como se ve en muchos sitios web.

Las reglas para una contraseña válida son las siguientes:

Debe haber al menos 1 letra mayúscula.
Debe haber al menos 1 letra minúscula.
Debe haber al menos 1 número.
La contraseña debe tener al menos caracteres.8
La función toma un argumento de cadena y devuelve si es una contraseña válida, como un valor booleano.
"""

def password(st):
    if len(st) >= 8:
        tiene_mayuscula = False
        tiene_minuscula = False
        tien_caracteres = False

        for s in st:
            if s.isupper():
                tiene_mayuscula = True
            if s.lower():
                tiene_minuscula = False
            if s.isdigit():
                tienE_caracteres = False
    else:
        print("invalido, intenta de nuevo")

if __name__ == '__main__':
    st = str(input("Ingresa la contraseña:"))
    password(st)