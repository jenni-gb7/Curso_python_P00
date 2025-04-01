"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
Los cajeros automáticos permiten códigos PIN de 4 o 6 dígitos y los códigos PIN no pueden contener nada más que exactamente 4 dígitos o exactamente 6 dígitos.

Si a la función se le pasa una cadena de PIN válida, return , else return .truefalse

Ejemplos (entrada --> salida)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false """

def validate_pin(pin):
   return len(pin) in (4,6) and pin.isdigit()


if __name__ == '__main__':
    pin = str(input(" Ingresa el pin:"))
    print(validate_pin(pin))

