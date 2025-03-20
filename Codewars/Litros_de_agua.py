"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
A Nathan le encanta el ciclismo.

Como Nathan sabe que es importante mantenerse hidratado, bebe 0,5 litros de agua por hora de ciclismo.

Se le da la hora en horas y debe devolver la cantidad de litros que Nathan beberá, redondeada hacia abajo.

Por ejemplo:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5
"""

print(" *** Litros de agua ***")


def litros(tiempo):
    return int(tiempo * 0.5)


if __name__ == '__main__':
    tiempo = float(input("Ingresa las horas:"))
    resultado = litros(tiempo)
    print(f"Tiempo:{tiempo} --->  Litros:{resultado}")