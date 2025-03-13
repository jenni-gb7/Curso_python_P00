"""
Nombre: Alberto Martínez Barbosa.
Fecha:
Descripción:
Primer ejemplo de uso de una clase y un objeto. En este caso, para representar a una persona.

Una clase es una plantilla o un plano para crear objetos.
Define un conjunto de atributos (datos) y métodos (funciones) que caracterizan a los objetos que se
crearán a partir de ella. Piensa en una clase como un molde que describe cómo serán los objetos.

* Atributos: Son variables que almacenan datos asociados a la clase.
* Métodos: Son funciones que definen el comportamiento de la clase.

"""


# Para crear una clase, se utiliza la palabra reservada "class", seguido del nombre (letra inicial en
# mayúsculas).
class Persona:
    """
    Clase que representa a una persona.
    Sus atributos son: nombre, edad, altura y peso.
    Sus métodos son: comer(), dormir() y caminar().
    """
    def __init__(self,nombre:str, edad: int, altura: float, peso: float):
        """
        Constructor de la clase Persona.
        :param nombre: Nombre completo de la persona.
        :param edad: Edad de la persona.
        :param altura: Altura (m) de la persona.
        :param peso: Peso (Kg) de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso


    def comer(self) -> None:
        """
        Función que indica que la persona está comiendo.
        """
        print(f"{self.nombre} está comiendo, seguramente va a subir de sus {self.peso:.2f} Kgs.")


    def dormir(self) -> None:
        """
        Función que indica que la persona está durmiendo.
        """
        print(f"{self.nombre} está durmiendo, por lo que va a ser un día mayor de sus {self.edad} años.")


    def caminar(self) -> None:
        """
        Función que indica que la persona está caminando.
        """
        print(f"{self.nombre} está caminando con sus {self.altura:.2f} metros de altura.")



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Se instancía (crea) un objeto de la clase Persona.
    # Nota: Crear un punto de ruptura en la condicional "if __name__ == "__main__"
    # y ejecutar en el modo depuración, probando con step over y step into.
    alberto = Persona("Alberto Martínez", 31, 1.66, 67.2)

    # Se imprimen los atributos del objeto.
    print("  -- Se crea un objeto de la clase Persona y se imprimen sus atributos:")
    print(f"Nombre: {alberto.nombre}. Edad: {alberto.edad}. "
          f"Altura: {alberto.altura}. Peso: {alberto.peso}. ")

    # Ahora se utilizan los métodos del objeto.
    print()
    print("  -- Se utilizan los métodos del objeto.")
    alberto.comer()
    alberto.dormir()
    alberto.caminar()

    # Se crea otro objeto de la clase Persona y se imprimen sus datos.
    cristiano = Persona("Cristiano Ronaldo", 40, 1.85, 83)

    print()
    print("  -- Nuevo objeto de la clase Persona:")
    print(f"Nombre: {cristiano.nombre}. Edad: {cristiano.edad}. "
          f"Altura: {cristiano.altura}. Peso: {cristiano.peso}. ")


    # Es posible actualizar la información de los atributos. En este caso, se modifican los datos
    # del primer objeto.
    print()
    print("  -- Actualización de los datos del objeto.")
    print("Datos previos:")
    print(f"Nombre: {alberto.nombre}. Peso: {alberto.peso}. ")

    alberto.nombre = "Alberto Martínez Barbosa"
    alberto.peso = 67.3

    print("Datos modificados:")
    print(f"Nombre: {alberto.nombre}. Peso: {alberto.peso}. ")