"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
Complete la función que devuelve el día de la semana de acuerdo con el número de entrada:

1 Devuelve "Sunday"
2 Devuelve "Monday"
3 Devuelve "Tuesday"
4 Devuelve "Wednesday"
5 Devuelve "Thursday"
6 Devuelve "Friday"
7 Devuelve "Saturday"
De lo contrario, devoluciones "Wrong, please enter a number between 1 and 7"""

def whatday(num):
    if num == 1:
        return "Sunday"
    elif num == 2:
        return "Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num == 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    elif num == 7:
        return "Saturday"
    else:
        return "Wrong, please enter a number between 1 and 7"




if __name__ == '__main__':
    num = int(input("Ingresa el número del dia:"))
    print(whatday(num))