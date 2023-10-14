#Clases= son moldes la estructura
#Objetos= se representa el objeto
#Instancias= se invoca (se crea el objeto)
#Metodos= son las acciones
#Atributos= son las caracteristicas

class Estudiante:
    def __init__(self):
        self.nombre=None
        self.apellido=None
        self.edad=None
        self.nacionalidad='Colombia'
    
    def entender(self):
        return 'Si, aprendí mucho hoy :)'


def main():
    estudiante=[]
    opc='n'
    while 1:
        est=Estudiante()
        est.nombre=input('Nombre: ')
        est.apellido=input('Apellido: ')
        est.edad=input('Edad: ')
        estudiante.append(est)
        opc=input('Desea salir? (y/n)')
        if opc=='y':
            break
        else:
            print('Invalido')
    
    print(f'-------Clase 2023-II -----\n')
    for i in estudiante:
        print(f'Nombre: {i.nombre} {i.apellido}\n\
            Edad: {i.edad}\n\n')
        
if __name__=="__main__":
    main()