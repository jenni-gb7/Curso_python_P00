"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:"""

class Scoreboard:
# __________________Constructor___________________________
    def __init__(self,points:int,text_color:tuple[int,int,int],font:str,size:float):
        self._points = points
        self._text_color = text_color
        self._font = font
        self._size = size
    def draw(self):
        pass
# -----------------Métodos de acceso---------
# Points
    @property
    def points(self) -> int:
        return self._points

    @points.setter
    def points(self, ppoints: int) -> None:
        self._points = ppoints
# text color
    @property
    def text_color(self) -> tuple:
        return self._text_color

    @text_color.setter
    def text_color(self, ttext_color: tuple) -> None:
        self._text_color = ttext_color
# front
    @property
    def font(self) -> str:
        return self._font

    @font.setter
    def font(self, ffont: str) -> None:
        self._front = ffont # Value
# size
    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, ssize: float) -> None:
        self._size = ssize # Value

    def __str__(self) -> float:
        return (f"points : {self.points}, Saldo:{self.saldo}")



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Se crean objetos de la clase y se imprime.
    print("  -- Se crean objetos de la clase Scoreboard.")

    print()
    print("Se crea un objeto sin argumentos:")
    marcador1 = Scoreboard()
    print(f"marcador1 = {marcador1}")

    print()
    print("Se crea otro objeto con (points, font y text_color) como argumentos por nombre:")
    marcador2 = Scoreboard(10, font="Arial", text_color= (127, 127, 127))
    print(f"marcador2 = {marcador2}")

    print()
    print("Se prueba el método draw() en ambos objetos:")
    marcador1.draw()
    marcador2.draw()