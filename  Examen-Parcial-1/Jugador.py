"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:
"""

class Jugador:
    """
    Clase que representa a un jugador.
    Atributos: nombre,número y goles anotados.
    Métodos:
    """

    def __init__(self,nombre:str,numero:int,goles: int = 0):
        ''' Se declaran los atributos protegidos'''
        self._nombre = nombre
        self._numero = numero
        self._goles = goles

    def anotar_goles(self,no_goles: int) -> None:
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


if __name__ == '__main__':
    juga1 = Jugador("Jose",2,3)
    print(juga1)
    no_goles = input("Ingresa los goles:")
    juga1.anotar_goles()