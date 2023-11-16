class Ciudadano():
    def __init__(self, nombre:str,idioma:str):
        self.__nombre=nombre
        self.__idioma=idioma
    
    #------- Setters --------
    def setNombre(self,nombre:str):
        self.__nombre = nombre

    def setIdioma(self,idioma:str):
        self.__idioma=idioma

    # ----- Getters -------
    def getNombre(self):
        return self.__nombre
    
    def getIdioma(self):
        return self.__idioma

    # ------- Sobrecarga --------
    def saludo(self):
        return "Quoi de beau!"
    
class Colombiano(Ciudadano):
    def __init__(self, nombre:str,idioma:str, cc:str):
        super().__init__(nombre, idioma)
        self.__cc=cc
    
    def setCC(self,cc:int):
        self.__cc=cc

    def getCC(self):
        return self.__cc
    
    #------- Sobrecarga --------
    def saludo(self):
        return "Qiubo y entonces"

class Inglaterra(Ciudadano):
    def __init__(self, nombre:str,idioma:str, id:str):
        super().__init__(nombre, idioma)
        self.__id=id
    
    def setId(self,id:int):
        self.__id=id

    def getId(self):
        return self.__id
    
    # ------- Sobrecarga --------
    def saludo(self):
        return "Hello my friend!"

class China(Ciudadano):
    def __init__(self):
        super().__init__()
        self.__shengfenzheng=None
    
    def setShengfenzheng(self,shengfenzheng:int):
        self.__shengfenzheng=shengfenzheng

    def getShengfenzheng(self):
        return self.__shengfenzheng
    
    # ------- Sobrecarga --------
    def saludo(self):
        return "你干嘛呀！!"

def darSaludo(obj):
    return obj.saludo()
    

def main():
    Colombianono = Colombiano()
    Colombianono.setNombre('Kevin')
    Colombianono.setIdioma('Español')
    Colombianono.setCC(1524348)

    ingles = Inglaterra()
    ingles.setNombre('Richard')
    ingles.setIdioma('English')
    ingles.setId(3937593)

    chino = China()
    chino.setNombre('Liu')
    chino.setIdioma('汉语')
    chino.setShengfenzheng(626525362)

    Ciudadano1 = Ciudadano()
    Ciudadano1.setNombre('Carla')
    Ciudadano1.setIdioma('Frances')

    #----- Aplicantes -----
    print(f'Aplicante: {Colombianono.getNombre()}\n'+\
        f'Idioma: {Colombianono.getIdioma()}\n' + \
            f'CC: {Colombianono.getCC()}\n'+
            darSaludo(Colombianono)+'\n')
    
    print(f'Aplicante: {ingles.getNombre()}\n'+\
        f'Idioma: {ingles.getIdioma()}\n' + \
            f'Id: {ingles.getId()}\n'+
            darSaludo(ingles)+'\n')

    print(f'Aplicante: {chino.getNombre()}\n'+\
        f'Idioma: {chino.getIdioma()}\n' + \
            f'省份证: {chino.getShengfenzheng()}\n'+
            darSaludo(chino)+'\n')

    print(f'Aplicante: {Ciudadano1.getNombre()}\n' + \
        f'Idioma: {Ciudadano1.getIdioma()}\n'+\
            darSaludo(Ciudadano1))

    

if __name__=="__main__":
    main()