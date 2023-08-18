print('Seleccione el codigo a ejecutar: \n\
 1.Abecerdario \n 2.Parqueadero \n 3.Tringulos')
Op=input('Ingrese alguna de las opciones anteriores: ')

if (Op=="1") or (Op.lower()=="abecedario" ):
        l=input('Ingrese una letra: ')
        if (l.lower()=="a" ):
            print('La',l,'es una Vocal')
        elif (l.lower()=="e" ):
            print('La',l,'es una Vocal')
        elif (l.lower()=="i" ):
            print('La',l,'es una Vocal')
        elif (l.lower()=="o" ):
            print('La',l,'es una Vocal')
        elif (l.lower()=="u" ):
            print('La',l,'es una Vocal')
        else:
            print('La',l,'es una consonante')

elif Op == "2" or Op.lower() == "parqueadero":
    t = float(input('Ingrese el tiempo de parqueo en minutos: '))
    va= t*139
    iva = va*0.19
    tot=va+iva
    total= round(tot,-1)
    if total%50!=0:
     total+=50-total%50
    print('A continuacion le dejamos su factura detallada: \n\
                         FACTURA\n\
    -----------------------------------------------------\n\
        Tiempo                          ',t,'minutos\n\
        Valor por minuto                 $ 139\n\
        Valor sin IVA                    $',va,'\n\
        IVA                              $',iva,'\n\
        Valor mas IVA incluido           $',tot,'\n\
        Total a Pagar                    $',total)
        
elif (Op=="3") or (Op.lower()=="triangulos" ):
        L1=int(input('Ingrese la longitud del lado 1: '))
        L2=int(input('Ingrese la longitud del lado 2: '))
        L3=int(input('Ingrese la longitud del lado 3: '))
        if  L1-L2<L3<L1+L2 or  L1-L3<L2<L1+L3 or L2-L3<L1<L2+L3:
            if L1==L2==L3:
                print('Es un triangulo Equilatero')
            elif L1==L2 and  L2!=L3 or L2==L3 and  L3!=L1 or L1==L3:
                print('Es un triangulo Isoseles')
            else:
                print('Es un triangulo Escaleno')
        else:
            print('El triangulo no se puede formar')
        
else:
    print('Ingrese un termino valido')