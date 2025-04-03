"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Clase que representa a un jugador en un torneo de fútbol.
"""


class Jugador:
    """
    Clase que representa a un jugador.

    Atributos:
        _nombre (str): Nombre del jugador.
        _numero (int): Número asignado al jugador.
        _goles (int): Cantidad de goles anotados por el jugador.

    Métodos:
        anotar_goles(no_goles: int) -> None: Suma una cantidad de goles al jugador.
        __str__() -> str: Devuelve una representación en cadena del jugador.
    """

    def __init__(self, nombre: str, numero: int, goles: int = 0):
        """Inicializa un jugador con nombre, número y goles anotados."""
        self._nombre = nombre
        self._numero = numero
        self._goles = goles

    def anotar_goles(self, no_goles: int) -> None:
        """Incrementa la cantidad de goles anotados por el jugador."""
        if no_goles > 0:
            self._goles += no_goles
        else:
            print("La cantidad de goles debe ser positiva.")

    # Métodos de acceso (Getters y Setters) para los atributos privados

    @property
    def nombre(self) -> str:
        """Obtiene el nombre del jugador."""
        return self._nombre

    @nombre.setter
    def nombre(self, nombrej: str) -> None:
        """Modifica el nombre del jugador."""
        self._nombre = nombrej

    @property
    def numero(self) -> int:
        """Obtiene el número del jugador."""
        return self._numero

    @numero.setter
    def numero(self, numeroj: int) -> None:
        """Modifica el número del jugador."""
        self._numero = numeroj

    @property
    def goles(self) -> int:
        """Obtiene la cantidad de goles anotados por el jugador."""
        return self._goles

    @goles.setter
    def goles(self, golesj: int) -> None:
        """Modifica la cantidad de goles anotados por el jugador."""
        self._goles = golesj

    def __str__(self) -> str:
        """Devuelve una representación en cadena del objeto."""
        return f"Nombre del jugador: {self.nombre}, Número: {self.numero}, Goles anotados: {self.goles}"
