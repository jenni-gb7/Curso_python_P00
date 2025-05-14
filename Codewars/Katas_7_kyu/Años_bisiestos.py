"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

def is_leap_year(year):
    return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

if __name__ == "__main__":
    year = int(input("Escribe un año entre 1600 y 4000: "))
    if is_leap_year(year):
        print(f"El año {year} es bisiesto.")
    else:
        print(f"El año {year} no es bisiesto.")
