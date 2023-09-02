def agregar(milista):
    num=int(input('¿Que desea agregar?: '))
    milista.append(num)
    print(milista)
def agregar(milista):
    inx=int('indique el indece: ')
    val=int(input('¿Que desea agregar?: '))
    milista.insert(inx,val)
    print(milista)    
def Formateo(milista):
    milista.clear()
    print(milista)   
    
def main(milista):
    print('Seleccione una opcion: \n',\
        '1.append')
    opc=input('seleccione: ')
    
    if opc=='1':
        

if __name__=="__main__":
    milista=[2,3,4,5]
    main(milista)