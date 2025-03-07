"""
Jennifer Marlene Gutiérrez Beteta
06 de febrero de 2025.
Descripción del programa:
"""

# Se crea al estudiante.
class Estudiante:   #La clases se escriben en mayuscula.
    def __init__(self,NombreE:str)->None:
        self.Nombre = NombreE
        self.Temas_aprendidos =[]
    def Aprender_tema(self,Tema: str)-> None:
        self.Temas_aprendidos.append(Tema)
        print(f"{self.Nombre} aprendió {Tema}")


class Profesor:
    def __init__(self,Nombre:str)->None:
        self.Nombre = Nombre
        self.Temas_dominados = []
    def Dominar_tema(self,Tema:str)->None:
        self.Temas_dominados.append(Tema)
        print(f"Temas dominados: {Tema}")
    def Enseñar_tema(No_tema:int)->str:
        self.Enseñar_Tema.append(No_tema)
        print(f"
# Revisar, falat el self y checar el subindice para la ultima función.