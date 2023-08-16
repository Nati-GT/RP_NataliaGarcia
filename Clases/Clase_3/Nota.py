nota=float(input('ingrese su nota: '))
if (nota>=0 and nota<=5):  
# if(0<=nota<=5):
    if nota>=3:
        print('Aprobo')
    else:
        print('Reprobo')
else:
    print('La nota ingresada es invalida')