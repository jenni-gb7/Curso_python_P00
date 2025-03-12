"""
Jennifer Marlene Gutiérrez Beteta
06 de febrero de 2025.
Descripción del programa: Atributos de instancia.
"""

# Se crea la clase estudiante.
class Estudiante:   #La clases se escriben en mayuscula.
    #__________________Constructor___________________________
    def __init__(self,Nombre:str)->None:
        self.Nombre = Nombre
        self.Temas_aprendidos =[]
    def aprender_tema(self,Tema: str)-> None:
        self.Temas_aprendidos.append(Tema)
        print(f"{self.Nombre} aprendió {Tema}")
    def __str__ (self)->str:
        return (f"Estudiante (Nombre:{self.Nombre},Temas aprendidos:{self.Temas_aprendidos}")

# Se crea la clase profesor.
class Profesor:
    # __________________Constructor___________________________
    def __init__(self,Nombre:str,Temas_dominados:list[str]):
        self.Nombre = Nombre
        self.Temas_dominados = Temas_dominados

    def dominar_tema(self,Tema:str)->None:
        self.Temas_dominados.append(Tema)
        print(f"Temas dominados: {Tema}")

    def enseñar_tema(self,No_tema:int)->str:
        if No_tema < len(self.Temas_dominados):
            return self.Temas_dominados[No_tema]
        else:
            return "Fuera de rango"

    def __str__(self) -> str:
        return (f"Profesor (Nombre:{self.Nombre},Temas aprendidos:{self.Temas_dominados}")


if __name__ == '__main__':
    Estudiante1 = Estudiante("Jennifer Marlene Gutiérrez Beteta")
    Estudiante2 = Estudiante("Rosalinda Aquino Perez")
    Estudiante1.aprender_tema("Evolución sitios web")
    Estudiante2.aprender_tema("Internet de las cosas")
    print(Estudiante1)
    print(Estudiante2)
    print()
    Profe= Profesor("Alberto",["Atributos de distancia","Evolución sitios web","Internet de las cosas"])
    print( Profe)
    Num_tema=Profe.enseñar_tema(0)
    print(Num_tema)
    print()
    Estudiante1.aprender_tema(Num_tema)
    Estudiante2.aprender_tema(Num_tema)
    print()
    # Tambien se pude hacer de la siguiente manera:
    Estudiante2.aprender_tema(Profe.enseñar_tema(1))


