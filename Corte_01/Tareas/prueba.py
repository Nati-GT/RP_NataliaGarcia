number=input(int('ingrese un numero: '))

if number%3==0:
    print('Pling')
elif number%5==0:
    print('Plang')
elif number%7==0:
    print('Plong')
elif number%3==0 and number%5==0:
    print('PlingPlang')
else:
    print(number)