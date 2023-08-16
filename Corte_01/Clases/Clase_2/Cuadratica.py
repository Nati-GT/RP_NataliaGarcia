import math as m #import math sqrt as rc

a=int(input('Ingrese el valor de A: '))
b=int(input('Ingrese el valor de B: '))
c=int(input('Ingrese el valor de C: '))
x1=(-b+m.sqrt((b**2)-(4*a*c)))/(2*a)
x2=(-b-m.sqrt((b**2)-(4*a*c)))/(2*a)
print('La solucion es ', x1, 'y', x2)