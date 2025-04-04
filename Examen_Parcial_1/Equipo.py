from Jugador import Jugador


class Equipo:
    """
    Clase que representa a un equipo en un torneo de fútbol.

    Atributos:
        id_Equipo (int): ID único del equipo generado automáticamente.
        _nombre_e (str): Nombre del equipo.
        _jugadores (list): Lista de jugadores que pertenecen al equipo.
        _id_equipo (int): Identificador único del equipo.

    Métodos:
        id_equipo: Obtiene el ID único del equipo.
        nombre_e: Obtiene o establece el nombre del equipo.
        agregar_jugadores: Agrega uno o más jugadores al equipo.
        remover_jugadores: Elimina uno o más jugadores del equipo.
        mostrar_jugadores: Muestra todos los jugadores del equipo.
        total_goles: Calcula y devuelve la cantidad total de goles anotados por el equipo.
        __str__: Devuelve una representación en cadena del equipo.
    """

    No_id = 1  # Variable estática para llevar el conteo de IDs de los equipos.

    def __init__(self, nombre_e: str, *jugadores: tuple[Jugador]):
        """
        Inicializa un equipo con un nombre y una lista de jugadores.
        """
        self.id_Equipo = Equipo.No_id
        Equipo.No_id += 1
        self._nombre_e = nombre_e
        self._jugadores = list(jugadores)
        self._id_equipo = self.id_Equipo

    @property
    def id_equipo(self) -> int:
        """
        Devuelve el ID único del equipo.
        """
        return self._id_equipo

    @property
    def nombre_e(self) -> str:
        """
        Devuelve el nombre del equipo.
        """
        return self._nombre_e

    @nombre_e.setter
    def nombre_e(self, nombre_eq: str) -> None:
        """
        Establece el nombre del equipo.
        """
        self._nombre_e = nombre_eq

    def agregar_jugadores(self, *jugadores: tuple[Jugador]) -> None:
        """
        Agrega uno o más jugadores al equipo.
        """
        self._jugadores.extend(jugadores)

    def remover_jugadores(self, *jugadores: tuple[Jugador]) -> None:
        """
        Elimina uno o más jugadores del equipo.
        """
        for jugador in jugadores:
            if jugador in self._jugadores:
                self._jugadores.remove(jugador)

    def mostrar_jugadores(self) -> None:
        """
        Muestra la lista de jugadores que pertenecen al equipo.
        """
        for jugador in self._jugadores:
            print(jugador)

    def total_goles(self) -> int:
        """
        Calcula y devuelve el total de goles anotados por los jugadores del equipo.
        """
        return sum(jugador.goles for jugador in self._jugadores)

    def __str__(self):
        """
        Devuelve una representación en cadena del equipo.
        """
        return f"ID: {self.id_Equipo}, Equipo: {self._nombre_e}, Goles Totales: {self.total_goles()}"

