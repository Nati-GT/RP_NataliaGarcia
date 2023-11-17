class Deportista():
    def __init__(self,nombre:str,edad:int,documento:str):
        self.__nombre=nombre
        self.__edad=edad
        self.__documento=documento

    #----------Setters------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setEdad(self,edad:int):
        self.__edad=edad

    def setDocumento(self,documento:str):
        self.__documento=documento

    #----------Getters------------
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad

    def getDocumento(self):
        return self.__documento
    
    def jugador(self):
        return f'{self.getNombre()} es un gran maestro ajedrecista'

class Futbolista(Deportista):
    def __init__(self, nombre:str,edad:int,documento:str,nombre_equipo:str,goles:int):
        super().__init__(nombre, edad, documento)
        self.nombre_equipo=nombre_equipo
        self.goles=goles
    
    #----------Setters-----------
    def setNombreEquipo(self,nombre_equipo:str):
        self.nombre_equipo=nombre_equipo

    def setGoles(self,goles:int):
        self.goles=goles
    
    #----------Getters-----------
    def getNombreEquipo(self):
        return self.nombre_equipo

    def getGoles(self):
        return self.goles
    
    #-----------Métodos-----------
    def patear(self):
        return f'El jugador {self.getNombre()} acaba de anotar un gol'
    
    def jugador(self):
        return f'{self.getNombre()} es un gran delantero'

class Tenista(Deportista):
    def __init__(self,nombre:str,edad:int,documento:str,set_ganados:int,ace:int):
        super().__init__(nombre, edad, documento)
        self.set_ganados=set_ganados
        self.ace=ace

    #----------Setters-----------
    def setSetGanados(self,set_ganados:int):
        self.set_ganados=set_ganados

    def setAce(self,ace:int):
        self.ace=ace
    
    #----------Getters-----------
    def getSetGanados(self):
        return self.set_ganados

    def getAce(self):
        return self.ace
    
    #----------Metodos-----------
    def Ace(self):
        return f'El jugador {self.getNombre()} acaba de hacer un punto'
    
    # def jugador(self):
    #     return f'{self.getNombre()} es un gran tenista'
    

def main():
    jugador1=Futbolista('Radamel Falcao García',35,'122343521','Colombia',34)
    jugador2=Tenista('Roger Federer',42,'887293643',6,12)
    jugador3=Deportista('Magnus Carlsen',32,'53543653')

    print(jugador2.jugador())
    print(jugador2.Ace())
    print('------------------')
    print(jugador1.jugador())
    print(jugador1.patear())
    print('------------------')
    print(jugador3.jugador())

if __name__=="__main__":
    main()