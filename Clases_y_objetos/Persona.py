"""
Jennifer Marlene Gutiérrez Beteta
05 de febrero de 2025.
Descripción del programa:
"""
# Se crea la persona.
class Persona:
    # Hace referencia a uno mismo, al objeto que se este utilizando, se crea una persona.
    def __init__(self,Nombre:str,Edad:int, Altura:float,Peso:float):
    # Atributos del objeto.
        self.Nombre = Nombre
        self.Edad = Edad
        self.Altura = Altura
        self.Peso = Peso
    def Caminar(self)-> None:
        print("Estoy caminando")
    def Comer(self)-> None:
        print("Estoy comiendo")
    def Jugar(self)-> None:
        print("Estoy jugando")
    def Dormir(self)-> None:
        print("Estoy durmiendo")

if __name__ == '__main__':
    Jennifer = Persona("Jennifer",19,1.52,46)
    print(Jennifer.Nombre)
    print(Jennifer.Edad)
    print(Jennifer.Altura)
    print(Jennifer.Peso)
    Jennifer.Caminar()
