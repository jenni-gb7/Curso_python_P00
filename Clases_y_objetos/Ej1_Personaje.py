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

    def __init__(self)-> None:
        """
        Constructor del empleado.
        :param X: Movimientos en x.
        :param Y: Movimientos en Y.
        """

        # Atributos de instancia.
        self.X = 0
        self.Y = 0

        # Se asigna el atributo de clase como atributo de instancia y luego se incrementa.
        # Nota: Para utilizar los atributos de clase, se utiliza el nombre de la clase seguido de un punto
        # y el nombre del atributo.
        self.id_Personaje = Personaje.No_id
        Personaje.No_id += 1

    def moverse(self,orden:str)-> None:
        for i in orden:
            if i == 'a' and self.Y <= 9:
                self.Y +=1
            elif  i == 'r' and self.Y  >= 1:
                self.Y -= 1
            elif i == 'd' and self.X <= 9:
                self.X += 1
            elif i == 'i' and self.X  >= 1:
                self.X -= 1

    def posicion_actual(self)-> None:
        print(f"Posición actual: (X,Y)= {self.X},{self.Y}")

    def __str__(self) -> str:
        return (f"Personaje id: {self.id_Personaje}, (X,Y): ({ self.X},{self.Y})")

if __name__ == '__main__':
    orden = None
    print("------Se crea el objeto de la clase Personaje y se imprime____\n")
    Personaje1 = Personaje()
    print(Personaje1)
    print()
    print("------Se solicita iterativamente las secuencias de movimiento____\n")
    while orden != 's':
        orden = input("Ingresa las ordenes de movimineto:")
        orden = orden.lower()   # Todas las letras ingresadas se convierten en minúsculas.
        print()
        Personaje1.moverse(orden)
        Personaje1.posicion_actual()

    print("Fin del programa.")



