"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa: Atributos de clases.
"""


# Se crea la clase Empleado.
class Empleado:
    no_id = 1   # Número de id (aidi, se usa como tipo contador.
    # __________________Constructor___________________________
    def __init__(self,Nombre:str,Sueldo:float)->None:
        self.Nombre = Nombre
        self.Sueldo = Sueldo
        self.id_Empleado = Empleado.no_id
        Empleado.no_id += 1

    def aumentar_sueldo(self,Porcentaje:float)->None:
        pass

    def __str__ (self)->str:
        return (f"Empleado id: {self.id_Empleado},Nombre:{self.Nombre},Sueldo:{self.Sueldo}")

class Empresa:
    # __________________Constructor___________________________
    def __init__(self, nombre: str, * empleados: Empleado) -> None:
        self.nombre = nombre
        self.empleados = list(empleados)
        Empleado.no_id += 1

    def agregar_empleados(self,* nuevos_empleados: Empleado)-> None:
        for empleado in list(nuevos_empleados):
            self.empleados.append(empleado)

    def mostrar_empleados(self) -> None:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        print(f"*** Lista de empleados de {self.nombre} ***")

        for empleado in self.empleados:
            print(empleado)

    def __str__(self) -> str:
        """
        Se utiliza para mostrar los empleados de la empresa en forma de lista.
        """
        # Se convierte los elementos de la lista en cadenas (invocando str() para cada uno de ellos) y
        # se unen con ", " a través del métod0 str.join().
        # Este patrón es muy común en Python para obtener una cadena a partir de una lista.
        empleados = ", ".join(str(empleado) for empleado in self.empleados)
        return f"Empresa({self.nombre = }, {empleados})"


if __name__ == '__main__':
    empleado1 = Empleado("Jose",200)
    empleado2 = Empleado("Maria", 250)
    Juan = Empleado("Juan", 250)


    unsij = Empresa("unsij",empleado1,empleado2)
    unsij.agregar_empleados(empleado1,empleado2)
    unsij.mostrar_empleados()
    print()
    print(unsij)# Def str
    print()
    print(Juan)
    Juan.Nombre = "Juan Bautista"
    print(Juan)