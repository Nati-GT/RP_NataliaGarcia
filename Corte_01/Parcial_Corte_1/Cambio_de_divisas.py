import random as r

def rates():
    a=r.randint(10,50)
    b=r.randint(10,50)
    c=r.randint(10,50)
    d=r.randint(10,50)
    e=r.randint(10,50)
    
    return a,b,c,d,e

def menu():
    print('Seleccione una de las siguientes opciones: \n\
 1.Conversion de COP a cualquier divisa seleccionada. \n\
 2.Ver las tasas de cambio y su correspondiente comision. ')
    


def main():
    usd=rates(a)
    eur=rates()
    cny=rates()
    jpy=rates()
    pen=rates()
    
    menu()

    Op=input('Ingrese alguna de las opciones anteriores: ')

    if (Op=="1") or (Op.lower()=="Conversion de COP a cualquier divisa seleccionada." ):
        print('1.USD \n 2.EUR \n 3.CNY \n 4.JPY \n 5.PEN' )
        n=int(input('Seleccione la divisa a cambiar: '))
        Ca=int(input('Cuanto desea cambia: '))
        if (n=="1") or (n.lower()=="usd" ):
            USD= Ca/4018
            pass
        elif (n=="2") or (n.lower()=="eur" ):
            EUR= Ca/4454
            print('En total son:',round(EUR,2))
            pass
        elif (n=="3") or (n.lower()=="cny" ):
            CNY= Ca/563
            print('En total son:',round(CNY,2))
            pass
        elif (n=="4") or (n.lower()=="jpy" ):
            JPY= Ca/28
            print('En total son:',round(JPY,2))
            pass
        elif (n=="5") or (n.lower()=="pen" ):
            PEN= Ca/1106
            print('En total son:',round(PEN,2))
        else:
            print('Seleccione una opcion valida')
        
            

    elif Op == "2" or Op.lower() == "Ver las tasas de cambio y su correspondiente comision.":
        print(f'divisa: USD, tasa: 4108, Comision: {usd}')
        print(f'divisa: EUR, tasa: 4108, Comision: {eur}')
        print(f'divisa: CNY, tasa: 4108, Comision: {cny}')
        print(f'divisa: JPY, tasa: 4108, Comision: {jpy}')
        print(f'divisa: PEN, tasa: 4108, Comision: {pen}')
        pass
    else:        
        print('Ingrese un termino valido')
            

if __name__=="__main__":
    main()
    