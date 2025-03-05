Generador de Nuevos Equipos

Descripción:
Este programa asigna miembros de diferentes equipos iniciales a nuevos equipos de 2 personas, asegurando que no se asignen dos personas que estuvieron en el mismo equipo inicialmente. Se generan 6 nuevos equipos con esta restricción.

Equipos Iniciales

El programa toma los siguientes equipos iniciales:

Los Algoritmos Anarquistas: Héctor, Addi, Jesús Alberto

Los Hackers de Café: Tania, Patricia, Rebeca

Los Codificadores Nocturnos: Jamileth, Bryan, Rosalinda

Los Ctrl+Z: Galilea, Jennifer, Juan

Funcionamiento del Programa

Unificación de Miembros: El programa comienza uniendo todos los miembros de los equipos iniciales en una lista.

Asignación de Nuevos Equipos:

El programa selecciona aleatoriamente dos miembros de la lista.
Se comprueba que los dos miembros seleccionados no provengan del mismo equipo inicial.
Si los dos miembros están en el mismo equipo inicial, el programa los devuelve a la lista y selecciona nuevamente dos miembros aleatorios.
Si los miembros son de equipos diferentes, se asignan a un nuevo equipo.
Creación de 6 Equipos: El proceso se repite hasta que se formen exactamente 6 equipos de 2 personas.

Resultado:
Los nuevos equipos estarán formados por 2 personas cada uno, sin que dos personas del mismo equipo inicial estén en el mismo equipo final.
