import math as m #import math sqrt as rc

a=int(input('Ingrese el valor de A: '))
b=int(input('Ingrese el valor de B: '))
c=int(input('Ingrese el valor de C: '))
raiz=b**2-4*a*c
if raiz>0:
    x1=(-b+m.sqrt((b**2)-(4*a*c)))/(2*a)
    x2=(-b-m.sqrt((b**2)-(4*a*c)))/(2*a)
    print('La solucion es ', x1, 'y', x2)
else:
    raiz=m.fabs(raiz)
    x_r=-b/(2*a)
    x_i=m.sqrt(raiz)/(2*a)
    print('Las soluciones son:\n'\
        ,x_r,'+',x_i,'i\n'\
        ,x_r,'-',x_i,'i')