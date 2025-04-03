from Equipo import Equipo


class Torneo:
    """
    Clase que representa un torneo de fútbol que involucra varios equipos.

    Atributos:
        _nombre (str): Nombre del torneo.
        _equipos (list): Lista de equipos que participan en el torneo.

    Métodos:
        nombre: Obtiene o establece el nombre del torneo.
        agregar_equipos: Agrega uno o más equipos al torneo.
        remover_equipos: Elimina uno o más equipos del torneo.
        mostrar_equipos: Muestra todos los equipos participantes en el torneo.
        generar_rol: Genera un rol de partidos estilo "todos contra todos", organizado por jornadas.
        __str__: Devuelve una representación en cadena del torneo y los equipos.
    """

    def __init__(self, nombre: str, *equipos: tuple[Equipo]):
        """
        Inicializa un torneo con un nombre y una lista de equipos.
        """
        self._nombre = nombre
        self._equipos = list(equipos)

    @property
    def nombre(self) -> str:
        """
        Devuelve el nombre del torneo.
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        """
        Establece el nombre del torneo.
        """
        self._nombre = nuevo_nombre

    def agregar_equipos(self, *equipos: tuple[Equipo]) -> None:
        """
        Agrega uno o más equipos al torneo.
        """
        self._equipos.extend(equipos)

    def remover_equipos(self, *equipos: tuple[Equipo]) -> None:
        """
        Elimina uno o más equipos del torneo.
        """
        for equipo in equipos:
            if equipo in self._equipos:
                self._equipos.remove(equipo)

    def mostrar_equipos(self) -> None:
        """
        Muestra todos los equipos que participan en el torneo.
        """
        for equipo in self._equipos:
            print(equipo)

    def generar_rol(self):
        """
        Genera un rol de partidos estilo "todos contra todos", organizado por jornadas.
        Si el número de equipos es impar, se agrega un descanso para uno de los equipos.
        """
        num_equipos = len(self._equipos)
        jornadas = []

        # Validar si hay suficientes equipos para generar el rol.
        if num_equipos < 2:
            print("No hay suficientes equipos para generar un rol de juegos.")
            return []

        equipos = self._equipos[:]
        if num_equipos % 2:
            equipos.append(None)  # Agregar un descanso si hay un número impar
            num_equipos += 1

        num_jornadas = num_equipos - 1
        for i in range(num_jornadas):
            jornada = []
            for j in range(num_equipos // 2):
                equipo1 = equipos[j]
                equipo2 = equipos[num_equipos - 1 - j]
                if equipo1 and equipo2:
                    jornada.append((equipo1, equipo2))
            jornadas.append(jornada)
            equipos.insert(1, equipos.pop())  # Rotar equipos

        return jornadas

    def __str__(self):
        """
        Devuelve una representación en cadena del torneo y los equipos.
        """
        return f"Torneo: {self._nombre}, Equipos: {[equipo.nombre_e for equipo in self._equipos]}"
