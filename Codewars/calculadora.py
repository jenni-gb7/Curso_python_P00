"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
Debe crear una calculadora simple que devuelva el resultado de la suma, resta, multiplicación o división de dos números.

La función aceptará tres argumentos:
El primer y el segundo argumento deben ser números.
El tercer argumento debe representar un signo que indique la operación a realizar sobre estos dos números.

Si las variables no son números o el signo no pertenece a la lista anterior, se debe devolver el mensaje "Valor desconocido".
"""

print("**** CALCULADORA ****")
print()

def menu_pri()-> None:
    print("== MENÚ PRINCIPAL ==")
    print(" ")
    print("[0].- Salir")
    print("[1].- Suma")
    print("[2].- Resta")
    print("[3].- Multiplicación")
    print("[4].- División")
    print(" ")
    opc = int(input("Ingresa una opción: "))
    return opc

def operaciones(opc,num1,num2)-> None:
    if opc == 1:
        resultado = num1 + num2
    elif opc == 2:
        resultado = num1 - num2
    elif opc == 3:
        resultado = num1 * num2
    elif opc == 4:
        resultado = num1 / num2
    else:
        print("No válido. Intenta de nuevo")
    return resultado

if __name__ == '__main__':
        opc = menu_pri()
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = operaciones(opc,num1,num2)
        print(f" Resultado: {resultado: .3f}")
