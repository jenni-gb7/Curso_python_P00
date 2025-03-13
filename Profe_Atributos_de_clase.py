"""
Nombre: Alberto Martínez Barbosa.
Fecha:
Descripción:
Ejemplo de uso de los atributos de clase.

Los atributos de clase son variables que pertenecen a la clase en sí, no a las instancias (objetos) de la clase.
Esto significa que todos los objetos comparten el mismo valor para estos atributos.
Úsalos para valores constantes, contadores, configuraciones globales o cualquier dato que deba ser compartido
entre todas las instancias de la clase.

"""

""" %%%%%%%     Clase    %%%%%%%%%%%%%%%%%%%%% """
class Empleado:
    """
    Clase que representa a un empleado.
    Sus atributos son: no_id (atributo de clase), nombre y sueldo.
    Sus métodos son: __init__(), __str__(), aumentar_sueldo().
    """

    # Atributo de clase. En este caso, se utiliza para generar ID de los empleados.
    no_id = 1

    def __init__(self, nombre: str, sueldo: float):
        """
        Constructor del empleado.
        :param nombre: Nombre del empleado.
        :param sueldo: Sueldo mensual del empleado.
        """

        # Atributos de instancia.
        self.nombre = nombre
        self.sueldo = sueldo

        # Se asigna el atributo de clase como atributo de instancia y luego se incrementa.
        # Nota: Para utilizar los atributos de clase, se utiliza el nombre de la clase seguido de un punto
        # y el nombre del atributo.
        self.id_empleado = Empleado.no_id
        Empleado.no_id += 1


    def aumentar_sueldo(self, porcentaje: float) -> None:
        """
        Se utiliza para aumentar el sueldo de acuerdo con un porcentaje.
        :param porcentaje: Porcentaje a incrementar el sueldo.
        """
        if porcentaje > 0:
            self.sueldo += self.sueldo * (porcentaje/100)
            print(f"El sueldo de {self.nombre} ahora es de {self.sueldo:,.2f}")

        else:
            print("No se aplicó ningún cambio, ya que por Ley, el sueldo no puede disminuir.")


    def __str__(self) -> str:
        """
        Se utiliza para definir la representación en cadena del empleado.
        :return: El objeto en forma de cadena.
        """
        return f"Empleado(id: {self.id_empleado}, Nombre: {self.nombre}, Sueldo: {self.sueldo:,.2f})"



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Ejemplo de uso de los atributos de clase.
    print("  -- Ejemplo de uso de los atributos de clase.")

    # Forma de acceder al atributo de clase.
    print(f"Atributo de clase: {Empleado.no_id = }")


    # Se crean varios objetos de la clase Empleado y se imprimen en consola.
    alberto = Empleado("Alberto Martínez", 1110.1)
    gerardo = Empleado("Gerardo Guerrero", 12_123.23)
    esteban = Empleado("Esteban Ramírez", 999.23)

    print()
    print("Se crean empleados:")
    print(alberto)
    print(gerardo)
    print(esteban)

    # Se muestra nuevamente el atributo de clase.
    print()
    print(f"Atributo de clase: {Empleado.no_id = }")