"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
Cree una función que tome 2 números enteros en forma de cadena como entrada y genere la suma (también como una cadena):
"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2"""

def sum_str(a, b):
    if a == "" :
        res = 0 + b
        return int(res)
    elif b == "" :
        res = a + 0
        return int(res)
    else:
        res = a + b
        return int(res)

if __name__ == '__main__':
    a = str(input("Ingresa el primer número:"))
    b = str(input("Ingresa el segundo número:"))
    print(sum_str(a, b))