class Ciudadano:
    def __init__(self):
        self.__nombre= None
        self.__apellido= None
        self.__documento= None
        self.__edad= None

    #-----------Setters----------
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setApellido(self,apellido:str):
        self.__apellido=apellido 

    def setDocumento(self, documento):
        while len(documento) < 8 or len(documento) > 10:
            print("Recuerde que el documento debe tener entre 8 y 10 dígitos.")
            documento = input("Ingrese el documento del ciudadano: ")
        self.__documento = documento

    def setEdad(self, edad):
        while edad <= 0:
            print("Recuerde que la edad debe ser un número positivo mayor que cero.")
            edad = int(input("Ingrese la edad del ciudadano: "))
        self.__edad = edad

    #-----------Getters--------------
    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getDocumento(self):
        return self.__documento

    def getEdad(self):
        return self.__edad

    # ---------- Verificacion si es Mayor de edad --------------
    def esMayorDeEdad(self):
        if self.getEdad() >= 18:
            return True
        return False

    #----------Sobrecarga Metodo--------------
    def reconocimientos(self):
        return 'No ha recibido ningun reconocimiento'

    def mostrar(self):
        return f"Nombre: {self.getNombre()} \n\
Apellido: {self.getApellido()} \n\
Edad: {self.getEdad()} \n\
Cédula: {self.getDocumento()}"


#-------------Clase Hijo Actor------------------
class Actor(Ciudadano):
    def __init__(self):
        super().__init__()
        self.setAñosDeProfesion(None)
        self.setObrasInterpretadas(None)
        self.setPapelesActuados(None)

    #-----------Setter hijo--------
    def setAñosDeProfesion(self,añosDeProfesion:int):
        self.__añosDeProfesion=añosDeProfesion 

    def setObrasInterpretadas(self,obrasInterpretadas:int):
        self.__obrasInterpretadas=obrasInterpretadas

    def setPapelesActuados(self,papelesActuados:int):
        self.__papelesActuados=papelesActuados

    #-----------Getters hijo----------
    def getAñosDeProfesion(self):
        return self.__añosDeProfesion

    def getObrasInterpretadas(self):
        return self.__obrasInterpretadas

    def getPapelesActuados(self):
        return self.__papelesActuados

    #----------Sobrecarga Metodo--------------
    def reconocimientos(self):
        return 'Ha sido convocado a obras importantes y ganado 3 premios'

    def mostrar(self):
        info_ciudadano = super().mostrar()
        return f"{info_ciudadano} \n\
Años de Profesión: {self.getAñosDeProfesion()} \n\
Obras Interpretadas: {self.getObrasInterpretadas()} \n\
Papeles Actuados: {self.getPapelesActuados()}"


#-------------Clase Hijo Escritor-----------------
class Escritor(Ciudadano):
    def __init__(self):
        super().__init__()
        self.setAñosDeEscritura(None)
        self.setLibrosPublicados(None)
        self.setGeneroDeEscritura(None)

    #-----------Setter hijo--------
    def setAñosDeEscritura(self,añosDeEscritura:int):
        self.__añosDeEscritura=añosDeEscritura
        
    def setLibrosPublicados(self,librosPublicados:int):
        self.__librosPublicados=librosPublicados

    def setGeneroDeEscritura(self,generoDeEscritura:str):
        self.__generoDeEscritura=generoDeEscritura

    #-----------Getters hijo----------
    def getAñosDeEscritura(self):
        return self.__añosDeEscritura

    def getLibrosPublicados(self):
        return self.__librosPublicados

    def getGeneroDeEscritura(self):
        return self.__generoDeEscritura
        
    #----------Sobrecarga Metodo--------------
    def reconocimientos(self):
        return 'Ha sido invitado a multiples eventos y a obtenido 5 premios'
    
    def mostrar(self):
        info_ciudadano = super().mostrar()
        return f"{info_ciudadano} \n\
Años de Escritura: {self.getAñosDeEscritura()} \n\
Libros Publicados: {self.getLibrosPublicados()} \n\
Género de Escritura: {self.getGeneroDeEscritura()}"


#-------------Clase Hijo Cantante-----------------
class Cantante(Ciudadano):
    def __init__(self):
        super().__init__()
        self.setAñosDeCarrera(None)
        self.setCancionesCompuestas(None)
        self.setGeneroMusical(None)

    #-----------Setter hijo-----------
    def setAñosDeCarrera(self, añosDeCarrera: int):
        self.__añosDeCarrera=añosDeCarrera

    def setCancionesCompuestas(self, cancionesCompuestas: int):
        self.__cancionesCompuestas=cancionesCompuestas

    def setGeneroMusical(self, generoMusical: str):
        self.__generoMusical=generoMusical

    #-----------Getters Hijo----------
    def getAñosDeCarrera(self):
        return self.__añosDeCarrera

    def getCancionesCompuestas(self):
        return self.__cancionesCompuestas

    def getGeneroMusical(self):
        return self.__generoMusical

    #----------Sobrecarga Metodo--------------
    def reconocimientos(self):
        return 'Es conocida a nivel mundial y ha obtenido 4 Grammys'
    
    def mostrar(self):
        info_ciudadano = super().mostrar()
        return f"{info_ciudadano} \n\
Años de Carrera: {self.getAñosDeCarrera()} \n\
Canciones Compuestas: {self.getCancionesCompuestas()} \n\
Género Musical: {self.getGeneroMusical()}"

def main():
    personas=[]
    while True:
        print('--------------¿Que tipo de Ciudadano desea agregar?--------------\n\
            1. Actor \n\
            2. Escritor \n\
            3. Cantante \n\
            4. Ciudadano normal\n')

        Op = input("Ingrese el número correspondiente: ")

        if Op == "1":
            actor = Actor()
            actor.setNombre(input("Ingrese el nombre del actor: "))
            actor.setApellido(input("Ingrese el apellido del actor: "))
            actor.setDocumento(input("Ingrese el documento del actor: "))
            actor.setEdad(int(input("Ingrese la edad del actor: ")))
            actor.setAñosDeProfesion(int(input("Ingrese años de profesión del actor: ")))
            actor.setObrasInterpretadas(int(input("Ingrese obras interpretadas por el actor: ")))
            actor.setPapelesActuados(int(input("Ingrese papeles actuados por el actor: ")))
            personas.append(actor)
            continuar=input("¿Desea agregar otro ciudadano? (Ingrese 'no' para terminar): ")
            if continuar.lower()=="no":
                break

        elif Op == "2":
            escritor = Escritor()
            escritor.setNombre(input("Ingrese el nombre del escritor: "))
            escritor.setApellido(input("Ingrese el apellido del escritor: "))
            escritor.setDocumento(input("Ingrese el documento del escritor: "))
            escritor.setEdad(int(input("Ingrese la edad del escritor: ")))
            escritor.setAñosDeEscritura(int(input("Ingrese años de escritura del escritor: ")))
            escritor.setLibrosPublicados(int(input("Ingrese libros publicados por el escritor: ")))
            escritor.setGeneroDeEscritura(input("Ingrese género de escritura del escritor: "))
            personas.append(escritor)
            continuar=input("¿Desea agregar otro ciudadano? (Ingrese 'no' para terminar): ")
            if continuar.lower()=="no":
                break
        
        elif Op == "3":
            cantante = Cantante()
            cantante.setNombre(input("Ingrese el nombre del cantante: "))
            cantante.setApellido(input("Ingrese el apellido del cantante: "))
            cantante.setDocumento(input("Ingrese el documento del cantante: "))
            cantante.setEdad(int(input("Ingrese la edad del cantante: ")))
            cantante.setAñosDeCarrera(int(input("Ingrese años de carrera del cantante: ")))
            cantante.setCancionesCompuestas(int(input("Ingrese canciones compuestas por el cantante: ")))
            cantante.setGeneroMusical(input("Ingrese género musical del cantante: "))
            personas.append(cantante)
            continuar=input("¿Desea agregar otro ciudadano? (Ingrese 'no' para terminar): ")
            if continuar.lower()=="no":
                break

        elif Op == "4":
            ciudadano=Ciudadano()
            ciudadano.setNombre(nombre=input("Ingrese el nombre del ciudadano: "))
            ciudadano.setApellido(apellido=input("Ingrese el apellido del ciudadano: "))
            ciudadano.setDocumento(documento=input("Ingrese la documento del ciudadano: "))
            ciudadano.setEdad(edad=int(input("Ingrese la edad del ciudadano: ")))        
            personas.append(ciudadano)
            continuar=input("¿Desea agregar otro ciudadano? (Ingrese 'no' para terminar): ")
            if continuar.lower()=="no":
                break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    for ciudadano in personas:
        print('--------------------Ciudadano--------------------')
        print(ciudadano.mostrar())
        if ciudadano.esMayorDeEdad():
            print(f"{ciudadano.getNombre()} es mayor de edad.")
        else:
            print(f"{ciudadano.getNombre()} no es mayor de edad.")
        print(ciudadano.reconocimientos())

if __name__ =="__main__":
    main()