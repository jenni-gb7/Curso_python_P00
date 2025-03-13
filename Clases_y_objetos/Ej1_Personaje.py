"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa:

Crea una clase llamada Personaje que simule los movimientos de un personaje de videojuegos en una ventana.

1. El personaje se moverá por una ventana de tamaño máximo (x, y) = (10, 10) y podrá realizar los siguientes movimientos si no supera el límite de la ventaja:
      * Avanzar (caracteres 'A' o 'a'): aumenta en 1 la posición en y,
      * Retroceder (caracteres 'R' o 'r'): disminuye en 1 la posición en y,
      * Derecha (caracteres 'D' o 'd'): aumenta en 1 la posición en x,
      * Izquierda (caracteres 'I' o 'i'): disminuye en 1 la posición en x.

2. El personaje tendrá los siguientes métodos (además de los métodos mágicos):
      * moverse() que recibe la orden como parámetro,
      * posicion_actual() que muestra en consola la posición en (x,y).

3. Se debe llevar un registro del ID de los personajes creados, por lo que se debe utilizar un atributo de clase.

4. Al crear los objetos de la clase, inicialmente deben establecerse en el origen (x, y) = (0, 0).

5. Se debe solicitar iterativamente la secuencia de movimientos e indicar la posición final de la secuencia.

6. El programa se detendrá con los caracteres 'S' o 's'..
"""

class Personaje:
    ''' Clase que representa a un personaje.
        Sus atributos son: id(atributo de clase), X y Y.'''

    # Atributo de clase. En este caso, se utiliza para generar ID de los empleados.
    No_id = 1

    def __init__(self,X:int,Y:int)-> None:
        """
        Constructor del empleado.
        :param X: Movimientos en x.
        :param Y: Movimientos en Y.
        """

        # Atributos de instancia.
        self.X = X
        self.Y = Y

        # Se asigna el atributo de clase como atributo de instancia y luego se incrementa.
        # Nota: Para utilizar los atributos de clase, se utiliza el nombre de la clase seguido de un punto
        # y el nombre del atributo.
        self.id_Personaje = Personaje.No_id
        Personaje.No_id += 1

    def ordenes(self,X:int,Y:int)-> None:
        pass

    def moverse(self):
        pass


    def __str__(self) -> str:
        return (f"Personaje id: {self.id_Personaje}")


    #-----------------    CÓDIGO A NIVEL DE MÓDULO ------------------------
if __name__ == '__main__':
    Personaje1 = Personaje("1","2")
    print(Personaje1)
    print(Personaje.No_id)
