"""
Jennifer Marlene Gutiérrez Beteta
10 de Abril de 2025.
5 de 7 kyu
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
    if len(st) < 8:
        return False
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_caracteres = False

    for s in st:
        if s.isupper():
            tiene_mayuscula = True
        if s.lower():
            tiene_minuscula = True
        if s.isdigit():
            tiene_caracteres = True

    if tiene_mayuscula == False or tiene_minuscula == False or tiene_caracteres == False:
        return False
    if tiene_mayuscula == False and tiene_caracteres == False:
        return False
    return True


if __name__ == '__main__':
    st = str(input("Ingresa la contraseña:"))
    password(st)