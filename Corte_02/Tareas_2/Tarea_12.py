class Ciudadano:
    def __init__(self,nombre:str,documento:int,edad:int):
        self.__nombre=nombre
        self.__documento=documento
        self.__edad=edad

    # ------------ Setters -----------
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setdocumento(self,documento:int):
        self.__documento=documento

    def setEdad(self,edad:int):
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
        print(f"Nombre: {self.__nombre} - Edad: {self.__edad} - Cédula: {self.__documento}")
        
    # ---------- Verificacion si es Mayor de edad --------------
    def esMayorDeEdad(self):
        if self.__edad >= 18:
            return True
        else:
            return False

def main():
    personas=[]
    while True:
        nombre=input("Ingrese el nombre del ciudadano: ")
        documento=input("Ingrese la documento del ciudadano: ")
        while len(documento)<8 or len(documento)>10:
            print("el documento debe tener entre 8 y 10 dígitos.")
            documento=input("Ingrese el documento del ciudadano: ")
        edad=int(input("Ingrese la edad del ciudadano: "))
        while edad<=0:
            print("La edad debe ser un número positivo mayor que cero.")
            edad=int(input("Ingrese la edad del ciudadano: "))
        ciudadano=Ciudadano(nombre, documento, edad)
        personas.append(ciudadano)
        continuar=input("¿Desea agregar otro ciudadano? (Ingrese 'no' para terminar): ")
        if continuar.lower()=="no":
            break

    for ciudadano in personas:
        print('--------------------Ciudadano--------------------')
        ciudadano.mostrar()
        if ciudadano.esMayorDeEdad():
            print(f"{ciudadano.getNombre()} es mayor de edad.")
        else:
            print(f"{ciudadano.getNombre()} no es mayor de edad.")

if __name__ =="__main__":
    main()
