class Ciudadano:
    def __init__(self):
        self.__nombre=None
        self.__documento=None
        self.__edad=None

    # ------------ Setters -----------
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setdocumento(self,documento:int):
        while len(documento)<8 or len(documento)>10:
            print("Recuerde que el documento debe tener entre 8 y 10 dígitos.")
            documento=input("Ingrese el documento del ciudadano: ")
        self.__documento=documento

    def setEdad(self,edad:int):
        while edad<=0:
            print("Recuerde que la edad debe ser un número positivo mayor que cero.")
            edad=int(input("Ingrese la edad del ciudadano: "))
        self.__edad=edad

    # ---------- Getters --------------
    def getNombre(self):
        return self.__nombre

    def getdocumento(self):
        return self.__documento

    def getEdad(self):
        return self.__edad
    
    # ---------- Metodo mostrar --------------
    def mostrar(self):
        return f"Nombre: {self.getNombre()} - Edad: {self.getEdad()} - Cédula: {self.getdocumento()}"
        
    # ---------- Verificacion si es Mayor de edad --------------
    def esMayorDeEdad(self):
        if self.getEdad() >= 18:
            return True
        return False

def main():
    personas=[]
    while True:
        ciudadano=Ciudadano()
        ciudadano.setNombre(nombre=input("Ingrese el nombre del ciudadano: "))
        ciudadano.setdocumento(documento=input("Ingrese la documento del ciudadano: "))
        ciudadano.setEdad(edad=int(input("Ingrese la edad del ciudadano: ")))        
        personas.append(ciudadano)
        continuar=input("¿Desea agregar otro ciudadano? (Ingrese 'no' para terminar): ")
        if continuar.lower()=="no":
            break

    for ciudadano in personas:
        print('--------------------Ciudadano--------------------')
        print(ciudadano.mostrar())
        if ciudadano.esMayorDeEdad():
            print(f"{ciudadano.getNombre()} es mayor de edad.")
        else:
            print(f"{ciudadano.getNombre()} no es mayor de edad.")

if __name__ =="__main__":
    main()
