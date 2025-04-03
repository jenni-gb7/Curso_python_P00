"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
Menú principal para gestionar jugadores, equipos y torneos.
"""

from Jugador import Jugador
from Equipo import Equipo
from Torneo import Torneo

# Listas
jugadores = []
equipos = []
torneo = Torneo("Torneo Principal")


def mostrar_menu():
    while True:
        print("\nMenú Principal")
        print("1. Crear jugadores")
        print("2. Crear equipos")
        print("3. Ver lista de jugadores")
        print("4. Ver lista de equipos")
        print("5. Agregar jugadores a un equipo")
        print("6. Eliminar jugadores de un equipo")
        print("7. Agregar equipos al torneo")
        print("8. Eliminar equipos del torneo")
        print("9. Anotar gol(es) a un jugador")
        print("10. Mostrar goles totales por equipo")
        print("11. Generar rol de juegos")
        print("12. Salir")

        opcion = validar_entrada_numeros("Seleccione una opción: ")

        if opcion == 1:
            crear_jugador()
        elif opcion == 2:
            crear_equipo()
        elif opcion == 3:
            ver_lista_jugadores()
        elif opcion == 4:
            ver_lista_equipos()
        elif opcion == 5:
            agregar_jugador_equipo()
        elif opcion == 6:
            eliminar_jugador_equipo()
        elif opcion == 7:
            agregar_equipos_torneo()
        elif opcion == 8:
            eliminar_equipo_torneo()
        elif opcion == 9:
            anotar_gol()
        elif opcion == 10:
            mostrar_goles_totales()
        elif opcion == 11:
            generar_rol_juegos()
        elif opcion == 12:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


# ----------------- FUNCIONES DEL MENÚ -----------------

def validar_entrada_letras(prompt):
    """Valida que la entrada solo contenga letras"""
    while True:
        entrada = input(prompt)
        if entrada.isalpha():  # Verifica si la entrada contiene solo letras
            return entrada
        else:
            print("Error: La entrada debe contener solo letras. Intente nuevamente.")


def validar_entrada_numeros(prompt):
    """Valida que la entrada sea un número entero positivo"""
    while True:
        entrada = input(prompt)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Error: La entrada debe ser un número. Intente nuevamente.")


def crear_jugador():
    nombre = validar_entrada_letras("Ingrese el nombre del jugador: ")
    numero = validar_entrada_numeros("Ingrese el número del jugador: ")
    goles = validar_entrada_numeros("Ingrese los goles anotados: ")

    jugador = Jugador(nombre, numero, goles)
    jugadores.append(jugador)

    print("\nJugador creado con éxito:")
    print(jugador)


def crear_equipo():
    nombre_e = validar_entrada_letras("Ingrese el nombre del equipo: ")
    equipo = Equipo(nombre_e)

    while True:
        nombre_j = input("Ingrese el nombre del jugador (o '' para terminar): ")
        if nombre_j.lower() == '':
            break
    equipos.append(equipo)

    print("\nEquipo creado con éxito:")
    print(equipo)


def ver_lista_jugadores():
    if not jugadores:
        print("No hay jugadores registrados.")
    else:
        for i, juga in enumerate(jugadores, 1):
            print(f"{i}. {juga}")


def ver_lista_equipos():
    if not equipos:
        print("No hay equipos registrados.")
    else:
        for i, equipo in enumerate(equipos, 1):
            print(f"{i}. {equipo}")

def agregar_jugador_equipo():
    ver_lista_equipos()
    nombre_e = input("Ingrese el nombre del equipo: ")
    equipo = Equipo(nombre_e)
    while True:
        nombre_j = input("Ingrese el nombre del jugador (o 'salir' para terminar): ")
        if nombre_j.lower() == 'salir':
            break
        else:
            nombre_j = input("Ingrese el nombre del jugador: ")
            numero_j = input("Ingrese el número del jugador: ")
            goles_j = input("Ingrese los goles anotados: ")

            jugador = Jugador(nombre_j, numero_j, goles_j)
            jugadores.append(jugador)

            equipo.agregar_jugadores(jugador)
            print(f"Jugador {nombre_j} agregado al equipo {nombre_e}\n")

        equipos.append(equipo)
    print("\nEquipo creado con éxito:")
    print(equipo)


def eliminar_jugador_equipo():
    pass

def validar_lista_numeros(mensaje, max_valor):
    """Solicita una lista de números separados por comas y los valida."""
    while True:
        entrada = input(mensaje)
        numeros = entrada.split(",")  # Separa los números por comas
        indices = []

        for num in numeros:
            num = num.strip()  # Elimina espacios en blanco
            if num.isdigit():  # Verifica que sea un número
                indice = int(num) - 1  # Convertir a índice de lista
                if 0 <= indice < max_valor:
                    indices.append(indice)
                else:
                    print(f" Error: El número {num} está fuera de rango.")
                    break
            else:
                print(f" Error: '{num}' no es un número válido.")
                break
        else:
            return indices  # Devuelve la lista si todos los valores fueron válidos

        print("⚠ Intente de nuevo.")



def agregar_equipos_torneo():
    ver_lista_equipos()
    indices = validar_entrada_numeros("Ingrese los índices de los equipos a agregar (separados por comas): ")

    for index in indices:
        if 0 <= index < len(equipos):
            torneo.agregar_equipos(equipos[index])

    print("Equipos agregados al torneo.")


def eliminar_equipo_torneo():
    torneo.mostrar_equipos()
    indices = validar_entrada_numeros("Ingrese los índices de los equipos a eliminar (separados por comas): ")

    for index in indices:
        if 0 <= index < len(torneo._equipos):
            torneo.remover_equipos(torneo._equipos[index])

    print("Equipos eliminados del torneo.")


def anotar_gol():
    ver_lista_jugadores()
    jugador_index = validar_entrada_numeros("Seleccione el índice del jugador: ") - 1

    if 0 <= jugador_index < len(jugadores):
        goles = validar_entrada_numeros("Ingrese la cantidad de goles a anotar: ")
        jugadores[jugador_index].anotar_goles(goles)
        print("Goles anotados correctamente.")
    else:
        print("Índice incorrecto.")


def mostrar_goles_totales():
    if not equipos:
        print("No hay equipos registrados.")
    else:
        for equipo in equipos:
            print(f"{equipo.nombre_e}: {equipo.total_goles()} goles")


def generar_rol_juegos():
    if not torneo._equipos:
        print("No hay suficientes equipos en el torneo.")
        return

    jornadas = torneo.generar_rol()

    print("\n📅Rol de Juegos:")
    for i, jornada in enumerate(jornadas, 1):
        print(f"\n🔹 Jornada {i}:")
        for partido in jornada:
            print(f"{partido[0].nombre_e} vs {partido[1].nombre_e}")


if __name__ == "__main__":
    mostrar_menu()