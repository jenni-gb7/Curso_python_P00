"""
Jennifer Marlene Gutiérrez Beteta
05 de Marzo de 2025.
Descripción del programa:
"""
# Se crea la persona.
class Persona:
    # Hace referencia a uno mismo, al objeto que se este utilizando, se crea una persona.
    def __init__(self,Nombre:str,Edad:int, Altura:float,Peso:float):    #Metodo constructor.
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
#-------------------------------------------------
    def Caminar(self)->None:
        print(f"{self.Nombre} esta caminando para bajar sus {self.Peso} kgs.")


if __name__ == '__main__':
    Jennifer = Persona("Jennifer",19,1.52,46)

    print(Jennifer.Nombre)
    print(Jennifer.Edad)
    print(Jennifer.Altura)
    print(Jennifer.Peso)
    #Jennifer = Peso = 42
    #Jennifer = Edad = 32
    #Jennifer.Caminar()
    print()
    Rosa = Persona("Rosa", 21, 1.50, 56)

    Rosa.Caminar()
    Rosa.Comer()
    Rosa.Jugar()
    Rosa.Dormir()








