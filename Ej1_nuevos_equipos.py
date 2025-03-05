'''Jennifer Marlene Gutiérrez Beteta
04 de febrero de 2025.
Descripción del programa:

El curso tiene los siguientes equipos:

Los Algoritmos Anarquistas: Héctor, Addi y Jesús Alberto.
Los Hackers de Café: Tania, Patricia, Rebeca.
Los Codificadores nocturnos: Jamileth, Bryan, Rosalinda.
Los Ctrl+Z: Galilea, Jennifer, Juan.

Este programa debe generar 6 nuevos equipos de 2 personas cada uno,
pero con la restricción de que no puede haber dos personas que ya
estuvieron en el mismo equipo de arriba ☝️.
'''

import random

print("")
print("*** NUEVOS EQUIPOS ***")
print("")

# Equipos iniciales
Algoritmos_Anarquistas = ["Héctor", "Addi", "Jesús Alberto"]
Hackers_de_Cafe = ["Tania", "Patricia", "Rebeca"]
Codificadores_nocturnos = ["Jamileth", "Bryan", "Rosalinda"]
Ctrl_Z = ["Galilea", "Jennifer", "Juan"]

# Unir todos los miembros en una sola lista.
todos_los_miembros = Algoritmos_Anarquistas + Hackers_de_Cafe + Codificadores_nocturnos + Ctrl_Z

# Crear una lista para los nuevos equipos vacíos.
nuevos_equipos = []

# Asignar miembros a los nuevos equipos de 2, evitando que personas del mismo equipo inicial estén juntas
while len(todos_los_miembros) > 1:  # Mientras haya al menos 2 personas
    # Elegir aleatoriamente dos personas
    miembro1 = random.choice(todos_los_miembros)
    todos_los_miembros.remove(miembro1)
    miembro2 = random.choice(todos_los_miembros)
    todos_los_miembros.remove(miembro2)

    # Comprobar que no estén en el mismo equipo inicial
    if (miembro1 in Algoritmos_Anarquistas and miembro2 in Algoritmos_Anarquistas) or \
       (miembro1 in Hackers_de_Cafe and miembro2 in Hackers_de_Cafe) or \
       (miembro1 in Codificadores_nocturnos and miembro2 in Codificadores_nocturnos) or \
       (miembro1 in Ctrl_Z and miembro2 in Ctrl_Z):
        # Si están en el mismo equipo inicial, devolverlos a la lista
        todos_los_miembros.append(miembro1)
        todos_los_miembros.append(miembro2)
        random.choice(todos_los_miembros)  # Mezclar de nuevo para elegir otros miembros
    else:
        # Si son de equipos diferentes, formamos un nuevo equipo
        nuevos_equipos.append([miembro1, miembro2])

# Mostrar los nuevos equipos
for i, equipo in enumerate(nuevos_equipos, 1):
    print(f"Equipo {i}: {equipo}")
