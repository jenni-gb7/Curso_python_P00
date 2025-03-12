"""
Jennifer Marlene Gutiérrez Beteta
11 de Marzo de 2025.
Descripción del programa: Atributos de clases.
"""
# Se crea la clase Empleado.
class Empleado:
    no_id = 0   # Número de id (aidi, se usa como tipo contador.
    # __________________Constructor___________________________
    def __init__(self,Nombre:str,Sueldo:float)->None:
        self.Nombre = Nombre
        self.Sueldo = Sueldo
        self.id = Empleado.no_id
        Empleado.no_id += 1

    def aumentar_sueldo(self,Porcentaje:float)->None:
        pass

    def __str__ (self)->str:
        return (f"Empleado id: {self.id},Nombre:{self.Nombre},Sueldo:{self.Sueldo}")


if __name__ == '__main__':
    Empleado1 = Empleado("Jose","$200")
    Empleado2 = Empleado("Maria", "$250")
    print(Empleado1)
    print(Empleado.no_id)