
class Personas:
    def __init__(self):
        self.nombre=None
        self.altura=None
        self.peso=None
    
    def Indice(self):
        IMC=int(self.peso)/((int(self.altura)/100)**2)
        if IMC <= 18.5:
            return str('Por debajo')
        elif IMC <=24.9:
            return str('Saludable')
        elif IMC <=29.9:
            return str('Sobrepeso')
        elif IMC <=34.9:
            return str('Obesidad I')
        elif IMC <=39.9:
            return str('Obesidad II')
        else:
            return str('obesidad III')

def main():
    Persona1 = Personas()
    Persona1.nombre='Leonardo Hamato'
    Persona1.altura=188
    Persona1.peso=97

    Persona2 = Personas()
    Persona2.nombre='Abril Oneil'
    Persona2.altura=160
    Persona2.peso=47

    Persona3 = Personas()
    Persona3.nombre='Cody Berns'
    Persona3.altura=158
    Persona3.peso=58

    Persona4 = Personas()
    Persona4.nombre='Kaitlyn Lopez'
    Persona4.altura=170
    Persona4.peso=73
    
    print(f'Persona: {Persona1.nombre} resultado: {Persona1.Indice()}')
    print(f'Persona: {Persona2.nombre} resultado: {Persona2.Indice()}')
    print(f'Persona: {Persona3.nombre} resultado: {Persona3.Indice()}')
    print(f'Persona: {Persona4.nombre} resultado: {Persona4.Indice()}')
    personas=[]
    opc='n'
    while 1:
        per=Personas()
        per.nombre=input('Nombre: ')
        per.altura=input('altura: ')
        per.peso=input('peso: ')
        personas.append(per)
        opc=input('Desea salir? (y/n)')
        if opc=='y':
            break
        else:
            print('Invalido')
    
    print(f'-------Personas Ingresadas Por El Usuario -----\n')
    for i in personas:
        print(f'Nombre: {i.nombre}\n\
        Altura: {i.altura}\n\
        Peso: {i.peso}\n\
        Su IMC es:',per.Indice())

if __name__=="__main__":
    main()