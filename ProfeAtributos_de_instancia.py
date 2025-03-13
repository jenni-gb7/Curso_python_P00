"""
Nombre: Alberto Martínez Barbosa.
Fecha:
Descripción:
Ejemplo de uso de los atributos de instancia y del métod0 especial __str__()

Los atributos de instancia son variables que pertenecen a un objeto específico (instancia) de una clase.
Estos atributos almacenan datos únicos para cada objeto y generalmente se definen en el métod0 __init__(),
que es el constructor de la clase.

El métod0 __str__() es un métod0 especial que se utiliza para definir la representación en forma de cadena
de texto (string) de un objeto. Este métod0 es llamado cuando se imprime un objeto con print().

"""


""" %%%%%%%     Clase    %%%%%%%%%%%%%%%%%%%%% """
class Estudiante:
    """
    Clase que representa a un estudiante.
    Sus atributos son: nombre (recibe como parámetro) y los temas que aprende.
    Sus métodos son: aprender_tema() y la representación en forma de cadena.
    """
    def __init__(self, nombre:str):
        """
        Constructor del estudiante.
        :param nombre: Nombre del estudiante.
        """
        # Los siguientes son atributos de instancia, ya que almacenan datos únicos para cada
        # objeto (instancia). En este caso, únicamente el atributo "nombre" se recibe como parámetro.
        self.nombre = nombre
        self.temas_aprendidos = []


    def aprender_tema(self,tema:str) -> None:
        """
        Se utiliza para añadir un tema a la lista de temas aprendidos.
        :param tema: Nuevo tema que va a aprender.
        """
        self.temas_aprendidos.append(tema)
        print(f"El tema '{tema}' ha sido aprendido por {self.nombre}!")


    # Nota: En una parte del código a nivel de módulo se pide poner entre comentarios a la siguiente función.
    def __str__(self) -> str:
        """
        Se utiliza para definir la representación en cadena de texto del objeto de la clase Estudiante.
        :return: El objeto en forma de cadena.
        """
        return f"Estudiante(Nombre: {self.nombre}, Temas aprendidos: {self.temas_aprendidos})"



""" %%%%%%%     Clase    %%%%%%%%%%%%%%%%%%%%% """
class Profesor:
    """
    Clase que representa a un profesor.
    Sus atributos son: nombre (recibe como parámetro) y los temas que domina.
    Sus métodos son: dominar_tema(), ensenar_tema() y la representación en forma de cadena.
    """
    def __init__(self, nombre:str, temas: list[str]):
        """
        Constructor del profesor.
        :param nombre: Nombre del profesor.
        :param temas: Lista de temas que domina.
        """
        self.nombre = nombre
        self.temas = temas.copy()   # Nota: Se utiliza una copia porque se pasan los argumentos por referencia.
                                    # De esta manera, se evita que los cambios repercutan en self.temas


    def dominar_tema(self,tema:str) -> None:
        """
        Se utiliza para añadir un tema a la lista de temas que domina el objeto de la clase Profesor.
        :param tema: Nuevo tema que va a dominar.
        """
        self.temas.append(tema)
        print(f"El tema '{tema}' ha sido dominado por {self.nombre}!")


    def ensenar_tema(self,no_tema: int) -> str:
        """
        Se utiliza para enseñar uno de los temas que domina el objeto de la clase Profesor.
        :param no_tema: El número del tema (posición).
        :return: El tema a enseñar.
        """
        if no_tema < len(self.temas):
            return self.temas[no_tema]

        else:
            return "Ese número de tema no se encuentra en la lista de temas dominados."


    def __str__(self) -> str:
        """
        Se utiliza para definir la representación en cadena de texto del objeto de la clase Profesor.
        :return: El objeto en forma de cadena.
        """
        return f"Profesor(Nombre: {self.nombre}, Temas dominados: {self.temas})"




""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == "__main__":
    # Se crea un objeto de la clase Estudiante y se realizan varios cambios de pruebas.
    estudiante_yared = Estudiante("Yared")
    print("  -- Se crea un objeto de la clase Estudiante y se realizan cambios en el objeto.")
    print("Se imprime el objeto creado:")
    print(estudiante_yared)     # Nota: Probar esta línea de código sin el métod0 __str__

    estudiante_yared.aprender_tema("Argumentos variables")
    estudiante_yared.aprender_tema("Clases y objetos")
    estudiante_yared.aprender_tema("Atributos de instancia")

    print()
    print("Se imprime el objeto con los cambios realizados:")
    print(estudiante_yared)


    # Se crea otro objeto de la clase Estudiante con otros atributos de instancia.
    print()
    print("  -- Se crea otro objeto de la clase Estudiante para probar que los atributos son diferentes.")

    estudiante_alberto = Estudiante("Alberto")
    estudiante_alberto.aprender_tema("Resistividad y conductancia")
    estudiante_alberto.aprender_tema("Ley de Ohm")

    print(estudiante_alberto)


    # Se crea un objeto de la clase Profesor para probar sus métodos.
    print()
    print("  -- Se crea un objeto de la clase Profesor para probar sus métodos.")

    profesor_oscar = Profesor("Óscar",["Tuplas","Listas","Diccionarios","Conjuntos"])
    print(profesor_oscar)


    # Se empieza a mostrar las relaciones entre objetos, en este caso, entre el profesor y los estudiantes.
    print()
    print("  -- Relación entre los objetos.")
    print("Estudiantes previo a aprender un tema:")
    print(estudiante_yared)
    print(estudiante_alberto)

    print()
    print(f"El profesor va enseñar el tema [3]: {profesor_oscar.ensenar_tema(3)}")
    estudiante_alberto.aprender_tema(profesor_oscar.ensenar_tema(3))
    estudiante_yared.aprender_tema(profesor_oscar.ensenar_tema(3))

    print()
    print("Estudiantes después de aprender un tema:")
    print(estudiante_yared)
    print(estudiante_alberto)