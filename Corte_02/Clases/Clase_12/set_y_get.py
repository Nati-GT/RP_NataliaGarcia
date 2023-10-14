class Estudiante:
    def __init__(self):
        self.__nombre=None
        self.__apellido=None
        self.__edad=None
        self.nacionalidad='Colombia'
    
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setApellido(self,apellido:str):
        self.__apellido=apellido

    def getApellido(self):
        return self.__apellido
    
    def setEdad(self,edad:int):
        self.__edad=edad

    def getEdad(self):
        return self.__edad

    def entender(self):
        return 'Si, aprendí mucho hoy :)'


def main():
    estudiante=[]
    opc='n'
    while 1:
        est=Estudiante()
        est.setNombre(input('Nombre: '))
        est.setApellido(input('Apellido: '))
        est.setEdad(int(input('Edad: ')))
        estudiante.append(est)
        opc=input('Desea salir? (y/n)')
        if opc=='y':
            break
        else:
            print('Invalido')
    
    print(f'-------Clase 2023-II -----\n')
    for i in estudiante:
        print(f'Nombre: {i.getNombre()} {i.getApellido()}\n\
            Edad: {i.getEdad()}\n\n')
        
if __name__=="__main__":
    main()