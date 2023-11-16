#--------------Clase Padre--------------
class Deportista():
    def __init__(self,nombre:str,documento:int,edad:int):
        self.__nombre= nombre
        self.__documento= documento
        self.__edad= edad
    #-----------Setters----------
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def setDocumento(self,documento:int):
        self.__documento=documento
    def setEdad(self,edad:int):
        self.__edad=edad
    #-----------Getters--------------
    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento
    def getEdad(self):
        return self.__edad
    
    # ------ Sobrecarga metodo -----
    def Jugador(self):
        return f'{self.getNombre()} es un gran jugador'
    
#-------- Clase Hijo ----------
class Futbolista(Deportista):
    def __init__(self, nombre: str, documento:int, edad: int,goles:int,nombre_equipo:str):
        super().__init__(nombre, documento, edad)
        self.__goles=goles
        self.__nombre_equipo=nombre_equipo
    # -------- Setters Hijo ----------
    def setGoles(self,goles:int):
        self.__goles=goles
    
    def setNombreEquipo(self,nombre_equipo:str):
        self.__nombre_equipo=nombre_equipo
    # ------- Getters Hijo ----------
    def getGoles(self):
        return self.__goles

    def getNombreEquipo(self):
        return self.__nombre_equipo
    # ------metodo -----
    def gol(self):
        return f'El jugador {self.getNombre()} acaba de anotar un gol'
    # ------ Sobrecarga metodo -----
    def Jugador(self):
        return f'{self.getNombre()} es un gran futbolista'


#-------- Clase Hijo ----------
class Tenista(Deportista):
    def __init__(self, nombre: str, documento:int, edad: int,set_ganados:int,ace:int):
        super().__init__(nombre, documento, edad)
        self.__set_ganados=set_ganados
        self.__ace=ace
    
    # -------- Setters Hijo ----------
    def setset_ganados(self,set_ganados:int):
        self.__set_ganados=set_ganados
    
    def setAce(self,ace:int):
        self.__ace=ace

    # ------- Getters Hijo ----------
    def getset_ganados(self):
        return self.__set_ganados

    def getAce(self):
        return self.__ace

    # ------metodo -----
    def Ace(self):
        return f'El jugador {self.getNombre()} acaba de hacer un punto'
    
    # ------ Sobrecarga metodo -----
    def Jugador(self):
        return f'{self.getNombre()} es un gran Tenista'


def main():
    Jugador=Futbolista('Falcao',24152637,35,34,'Selección Colombia')
    print(f'Deportista: {Jugador.getNombre()}\n'+\
    f'Documento:{Jugador.getDocumento()}\n'+\
    f'Edad:{Jugador.getEdad()}\n'+\
    f'Cantidad de Goles:{Jugador.getGoles()}\n'+\
    f'Equipo:{Jugador.getNombreEquipo()}\n'+\
    f'Gol:{Jugador.gol()}\n')
    
    Jugador2=Tenista('Roger Federer','263663737',42,6,12)
    print(f'Deportista: {Jugador2.getNombre()}\n'+\
    f'Documento:{Jugador2.getDocumento()}\n'+\
    f'Edad:{Jugador2.getEdad()}\n'+\
    f'Sets:{Jugador2.getset_ganados()}\n'+\
    f'Ace:{Jugador2.getAce()}\n'+\
    f'Ace:{Jugador2.Ace()}')

if __name__=="__main__":
    main()