"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
Clase del equipo
"""

class Equipo:
    """
        Clase que representa a un jugador.
        Atributos: nombre,número y goles anotados.
        Métodos:
        """
    No_id = 1
    def __init__(self,nombre_e: str, *jugadores: tuple [Jugador]):
        ''' Se declaran los atributos protegidos'''
        self.id_Equipo = Equipo.No_id
        Equipo.No_id += 1
        self._nombre_e = nombre_e
        self._jugadores= list(jugadores)
        self._id_equipo = id_equipo


    def anotar_goles(self, no_goles: int) -> None:
        self.no_goles = no_goles + no_goles
        print(f" No_goles = {self.no_goles}")
        # -----------------Métodos de acceso---------

    ''' Permiten acceder y modificar los atributos.'''

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def points(self, nombrej: str) -> None:
        self._nombre = nombrej

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, numeroj: int) -> None:
        self._numero = numeroj

    @property
    def goles(self) -> int:
        return self._goles

    @goles.setter
    def goles(self, golesj: int) -> None:
        self._goles = golesj

    def __str__(self) -> str:
        ''' Devuelve una representación en cadena del objeto.'''
        return (f" Nombre del jugador: {self.nombre}, Número: {self.numero}, Goles anotados:{self.goles}")
