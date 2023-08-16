print('Seleccione el codigo a ejecutar: \n\
 1.Matrix \n 2.Conversion \n 3.Temperatura \n\
 4.Iva')
Op=input('Ingrese alguna de las opciones anteriores: ')

if (Op=="1") or (Op.lower()=="matrix" ):
        n=input('Ingrese su nombre: ')
        print('Estas en la Matrix,',n)
elif (Op=="2") or (Op.lower()=="conversion" ):
        p=float(input('Ingrese la medida en pulgadas: '))
        mi=p*(25.4) 
        print('La medida',p,'pulgadas es igual a',round(mi,2),'milimetros')
elif (Op=="3") or (Op.lower()=="Temperatura" ):
        f=float(input('Ingrese una temperatura en grados Frenheit: '))
        c=(f-32)/1.8
        print(f,'grados Farenheit es igual a',round(c,2),'grados celsius')
elif (Op=="4") or (Op.lower()=="iva" ):
        v=float(input('Ingrese el valor de un producto: '))
        iva=v*0.19
        vb=v-iva
        print('El valor del Iva de',v,'es',round(iva,2),'y el valor bruto del producto es',round(vb,2))
else:
    print('Ingrese un termino valido')