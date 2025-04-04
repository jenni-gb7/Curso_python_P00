# Jennifer Marlene Gutiérrez Beteta
# 11 de Marzo de 2025.
# Programa para gestionar jugadores, equipos y torneos desde un menú.

from Jugador import Jugador
from Equipo import Equipo
from Torneo import Torneo
import re

# Listas donde se guardan los jugadores y equipos
jugadores = []
equipos = []
torneo = Torneo("Torneo Principal")

# ---------------- MENÚ PRINCIPAL ----------------
def mostrar_menu():
    while True:
        print("\nMenú Principal")
        print("1. Crear jugadores")
        print("2. Crear equipos")
        print("3. Ver lista de jugadores")
        print("4. Ver lista de equipos")
        print("5. Agregar jugadores a un equipo")
        print("6. Quitar jugadores de un equipo")
        print("7. Agregar equipos al torneo")
        print("8. Quitar equipos del torneo")
        print("9. Anotar goles a un jugador")
        print("10. Ver goles por equipo")
        print("11. Crear partidos del torneo")
        print("12. Salir")

        opcion = validar_entrada_numeros("Elige una opción: ")

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
            eliminar_equipos_torneo()
        elif opcion == 9:
            anotar_gol()
        elif opcion == 10:
            mostrar_goles_totales()
        elif opcion == 11:
            generar_rol_juegos()
        elif opcion == 12:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta otra vez.")


# -------- FUNCIONES DE VALIDACIÓN --------
def validar_entrada_letras(texto):
    while True:
        entrada = input(texto)
        if re.fullmatch(r"[A-Za-zÁ-ú ]+", entrada.strip()):
            return entrada.strip()
        else:
            print("Solo se permiten letras y espacios.")


def validar_entrada_numeros(texto):
    while True:
        entrada = input(texto)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Debes ingresar un número.")


def validar_lista_numeros(texto, max_valor):
    while True:
        entrada = input(texto)
        numeros = entrada.split(",")
        indices = []

        for num in numeros:
            num = num.strip()
            if num.isdigit():
                indice = int(num) - 1
                if 0 <= indice < max_valor:
                    indices.append(indice)
                else:
                    print(f"El número {num} está fuera de rango.")
                    break
            else:
                print(f"'{num}' no es un número válido.")
                break
        else:
            return indices

        print("Vuelve a intentarlo.")


# -------- FUNCIONES DEL MENÚ --------
def crear_jugador():
    nombre = validar_entrada_letras("Nombre del jugador: ")
    numero = validar_entrada_numeros("Número del jugador: ")
    goles = validar_entrada_numeros("Cantidad de goles: ")

    jugador = Jugador(nombre, numero, goles)
    jugadores.append(jugador)
    print("Jugador creado con éxito.")


def crear_equipo():
    nombre_e = validar_entrada_letras("Nombre del equipo: ")
    equipo = Equipo(nombre_e)
    equipos.append(equipo)
    print("Equipo creado con éxito.")


def ver_lista_jugadores():
    if not jugadores:
        print("No hay jugadores.")
    else:
        for i, j in enumerate(jugadores, 1):
            print(f"{i}. {j}")


def ver_lista_equipos():
    if not equipos:
        print("No hay equipos.")
    else:
        for i, e in enumerate(equipos, 1):
            print(f"{i}. {e}")


def agregar_jugador_equipo():
    ver_lista_equipos()
    nombre_e = input("Nombre del equipo: ").strip()

    equipo = next((e for e in equipos if e.nombre_e.lower() == nombre_e.lower()), None)

    if equipo:
        ver_lista_jugadores()
        jugador_index = validar_entrada_numeros("Número del jugador: ") - 1

        if 0 <= jugador_index < len(jugadores):
            jugador = jugadores[jugador_index]
            equipo.agregar_jugadores(jugador)
            print(f"{jugador.nombre} agregado a {equipo.nombre_e}")
        else:
            print("Número de jugador incorrecto.")
    else:
        print("No se encontró el equipo.")


def eliminar_jugador_equipo():
    ver_lista_equipos()
    nombre_e = input("Nombre del equipo: ").strip()

    equipo = next((e for e in equipos if e.nombre_e.lower() == nombre_e.lower()), None)

    if equipo:
        if not equipo.jugadores:
            print("Ese equipo no tiene jugadores.")
            return

        print(f"\nJugadores en {equipo.nombre_e}:")
        for i, j in enumerate(equipo.jugadores, 1):
            print(f"{i}. {j.nombre} (#{j.numero})")

        jugador_index = validar_entrada_numeros("Número del jugador a quitar: ") - 1

        if 0 <= jugador_index < len(equipo.jugadores):
            eliminado = equipo.jugadores.pop(jugador_index)
            print(f"{eliminado.nombre} fue eliminado del equipo.")
        else:
            print("Número incorrecto.")
    else:
        print("No se encontró el equipo.")


def agregar_equipos_torneo():
    ver_lista_equipos()
    nombre_e = input("Nombre del equipo a agregar al torneo: ").strip()

    if nombre_e:
        nuevo_equipo = Equipo(nombre_e)
        torneo.agregar_equipos(nuevo_equipo)
        print(f"{nombre_e} agregado al torneo.")


def eliminar_equipos_torneo():
    if not torneo._equipos:
        print("No hay equipos en el torneo.")
        return

    print("\nEquipos en el torneo:")
    torneo.mostrar_equipos()

    indices = validar_lista_numeros("Escribe los números de los equipos a eliminar (separados por coma): ", len(torneo._equipos))

    if not indices:
        print("No se eliminó ningún equipo.")
        return

    for index in sorted(indices, reverse=True):
        eliminado = torneo._equipos.pop(index)
        print(f"{eliminado.nombre_e} eliminado del torneo.")

    print("Equipos eliminados correctamente.")


def anotar_gol():
    ver_lista_jugadores()
    jugador_index = validar_entrada_numeros("Número del jugador: ") - 1

    if 0 <= jugador_index < len(jugadores):
        goles = validar_entrada_numeros("¿Cuántos goles anotar?: ")
        jugadores[jugador_index].anotar_goles(goles)
        print("¡Goles anotados!")
    else:
        print("Número incorrecto.")


def mostrar_goles_totales():
    if not equipos:
        print("No hay equipos.")
    else:
        for equipo in equipos:
            print(f"{equipo.nombre_e}: {equipo.total_goles()} goles")


def generar_rol_juegos():
    jornadas = torneo.generar_rol()
    if not jornadas:
        return

    print("\nRol de Juegos:")
    for i, jornada in enumerate(jornadas, 1):
        print(f"\nJornada {i}:")
        for partido in jornada:
            print(f"{partido[0].nombre_e} vs {partido[1].nombre_e}")


if __name__ == "__main__":
    mostrar_menu()
