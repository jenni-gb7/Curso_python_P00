"""
Jennifer Marlene Gutiérrez Beteta
24 de Marzo de 2025.
Descripción del programa:"""
from Clases_y_objetos.Ej1_Scoreboard import Scoreboard

class Window:
    # __________________Constructor___________________________
    def __init__(self,title:str = "Buscaminas",width:int = 800,height:int = 900,scoreboard : Scoreboard = Scoreboard()):
        self._title = title
        self._width = width
        self._height = height
        self._scoreboard = scoreboard

    def draw_scoreaboard(self)->None:
        pass

    def update_scoreaboard(self,points: int)-> None:
        pass

    # -----------------Métodos de acceso---------
#title
    @property
    def title(self) -> int:
        return self._title

    @title.setter
    def title(self, ttitle: int) -> None:
        self._title = ttitle

#width
    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def twidth(self, wwidth: int) -> None:
        self._twidth = wwidth
# height
    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, hheight:int) -> None:
        self._height = hheight

#scoreaboard
    @property
    def scoreaboard(self) -> int:
        return self._scoreboard

    @scoreaboard.setter
    def twidth(self, sscoreboard: int) -> None:
        self._scoreboard = sscoreboard

    def __str__(self)->str:
        return (f"Windows(title = {self.title}, width = {self.width}, height=  {self.height}, scoreboard = (points = {self._scoreboard.points}, text_color = {self._scoreboard.text_color}, font = {self._scoreboard.font}, size = {self._scoreboard.size}")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
"""Importar el ejercicio 2 de scoreboard"""

if __name__ == "__main__":
    # Se crean objetos de la clase Window sin un objeto de la clase Scoreboard creado
    # y se prueban sus métodos.
    print("  -- Se crea un objeto de la clase Window sin un objeto de la clase Scoreboard.")

    buscaminas = Window("Buscaminas", 800, 900)

    print("Se imprime el objeto:")
    print(f"Buscaminas = {buscaminas}")

    print()
    print("Método para dibujar el scoreboard:")
    buscaminas.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    buscaminas.update_score(1)


    # Se crean objetos de ambas clases y se prueban sus métodos.
    print()
    print("  -- Se crea otro objeto de la clase Window, pero ahora con un objeto de la clase Scoreboard.")

    marcador_solitario = Scoreboard(10,(40, 40, 40), "Arial", 40)
    solitario = Window("Solitario", 1_000, 1_000, marcador_solitario)

    print("Se imprimen los objetos:")
    print(f"marcador_solitario = {marcador_solitario}")
    print(f"Solitario = {solitario}")

    print()
    print("Método para dibujar el scoreboard:")
    solitario.draw_scoreboard()
    print()
    print("Método para actualizar el scoreboard:")
    solitario.update_score(11)


    # Se modifican los atributos mediante los métodos de acceso.
    print()
    print("  -- Se modifican los atributos mediante los métodos de acceso.")

    print("Se tiene la ventana buscaminas:")
    print(f"buscaminas = {buscaminas}")
    print("Se reemplaza el scoreboard utilizando el setter:")
    buscaminas.scoreboard = marcador_solitario
    print(f"buscaminas = {buscaminas}")