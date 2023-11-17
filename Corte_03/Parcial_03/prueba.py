"""Natalia Valentina Garcia Torres y Laura Valeria Jerez Bayona"""
#--------------Clase Padre--------------
class ConversorNumerico():
    def __init__(self):
        self.__numero = None

    def setNumero(self, numero):
        self.__numero = numero

    def getNumero(self):
        return self.__numero

#--------------Clase hijo Decimal-------------
class Decimal(ConversorNumerico):
    def __init__(self):
        super().__init__()

    def setNumero(self, numero):
        # No es necesario pedir el número aquí si se hereda de la clase padre
        super().setNumero(numero)

    def getDecbin(self, numero=None):  # Ajuste en el método getDecbin
        if numero is None:
            numero = self.getNumero()

        conversion = ''
        if numero > 1:
            conversion = self.getDecbin(numero // 2)
        return conversion + str(numero % 2)

    def getDechex(self):
        numero = self.getNumero()
        hex_chars = "0123456789ABCDEF"
        conversion = ''
        while numero > 0:
            conversion = hex_chars[numero % 16] + conversion
            numero = numero // 16
        return conversion
    
    def resultadoDecbin(self):
        return f'El numero decimal {self.getNumero} es {self.getDecbin} en binario'
    
    def resultadoDechex(self):
        return f'El numero decimal {self.getNumero} es {self.getDechex} en binario'
    
#--------------Clase Hijo Binario--------------
class Binario(ConversorNumerico):
    def __init__(self,numero:int, bindec:int):
        super().__init__(numero)
        self.__bindec=bindec

    def setBindec(self,bindec:int):
        numero=str('numero')
        convercion=[]
        tot=[]
        for i in numero:
            convercion.append(i)
        for j in range(len(convercion)):
                tot.append(int(convercion[j])*(2**(len(convercion)-int(j+1))))
        print(sum(tot))
        self.__bindec=bindec

    def getBindec(self):
        return self.__bindec
    
#--------------Clase Hijo Hexadecimal--------------
class Hexadecimal(ConversorNumerico):
    def __init__(self,numero:int, hexadecimal:int):
        super().__init__(numero)
        self.__hexadecimal=hexadecimal

    def setHexadecimal(self,hexadecimal:int):
        numero=str(numero)
        convercion = []
        tot = []
        for i in numero:
            if i == "a":
                i = 10
            elif i == "b":
                i = 11
            elif i == "c":
                i = 12
            elif i == "d":
                i = 13
            elif i == "e":
                i = 14
            elif i == "f":
                i = 15
            convercion.append(i)
        for j in range(len(convercion)):
                tot.append(int(convercion[j])*(16**(len(convercion)-int(j+1))))
        print(sum(tot))
        self.__hexadecimal=hexadecimal

    def getHexadecimal(self):
        return self.__hexadecimal

def main():
    while True:
        print('--------------Sistema de conversión numérico--------------\n'
              '1. Conversión Decimal a Binario\n'
              '2. Conversión Decimal a Hexadecimal\n'
              '3. Conversión Binario a Decimal\n'
              '4. Conversión Hexadecimal a Decimal\n')

        Op = input('¿Qué conversión desea realizar? (Ingrese el número de la opción): ')
        
        convertir = ConversorNumerico()
        numero = int(input('Escriba el número a convertir: '))
        convertir.setNumero(numero)
        
        if Op == "1":
            decimal = Decimal()
            decimal.setNumero(numero)
            print(f'El número decimal {convertir.getNumero()} es {decimal.getDecbin()} en binario')

        elif Op == "2":
            decimal = Decimal()
            decimal.setNumero(numero)
            print(f'El número decimal {convertir.getNumero()} es {decimal.getDechex()} en hexadecimal')
        elif Op=="3":
            binario=Binario()
            print(f'El numero Binario {ConversorNumerico.getNumero()} es {Binario.getBindec}')
        
        elif Op=="4":
            hexa=Hexadecimal()
            print(f'El numero Hexadecimal {ConversorNumerico.getNumero()} es {Hexadecimal.getHexadecimal}')
            break
        else:
            print('opcion invalida')
            

if __name__ =="__main__":
    main()