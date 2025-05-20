"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
Cree una función finalGrade, que calcula la calificación final de un estudiante en función de dos parámetros: una calificación para el examen y un número de proyectos completados.

Esta función debe tomar dos argumentos: Examen - Calificación del examen (de 0 a 100); proyectos - número de proyectos completados (desde 0 en adelante);

Esta función debe devolver un número (calificación final). Existen cuatro tipos de calificaciones finales:

100, si la calificación del examen es superior a 90 o si el número de proyectos finalizados supera 10.
90, si la calificación del examen es superior a 75 y si el número de proyectos finalizados es de un mínimo de 5.
75, si la calificación del examen es superior a 50 y si el número de proyectos finalizados es de un mínimo de 2.
0, en otros casos.

100, 12 --> 100
99, 0 --> 100
10, 15 --> 100

85, 5 --> 90

55, 3 --> 75

55, 0 --> 0
20, 2 --> 0"""

def final_grade(exam, projects):
    """
    Calcula la calificación final de un estudiante basada en el examen y los proyectos completados.
    Parámetros: exam (int): Calificación del examen (de 0 a 100).
    projects (int): Número de proyectos completados.
    Retorna: int: Calificación final según las reglas descritas.
        """
    if (exam >= 90 or projects > 10):
        return 100
    elif exam >= 75 and projects >= 5:
        return 90
    elif exam >= 50 and projects >= 2:
        return 75
    else:
        return 0


if __name__ == '__main__':
    exam = int(input("Ingresa la calificación del examen:"))
    projects = int(input("Ingresa el número de proyectos finaizados:"))
    print(final_grade(exam, projects))