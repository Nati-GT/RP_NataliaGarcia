# print("Seleccione una opción:\n", \
#       "1. Realizar un triangulo equilatero\n",\
#         "2. Realizar un triangulo isósceles\n", \
#             "3.Realizar un triangulo escaleno")


print("Por favor ingrese 3 longitudes")
a = int(input("longitud 1: "))
b = int(input("longitud 2: "))
c = int(input("longitud 3: "))
if a + c > b and a + b > c and c + b > a:
    if a == b == c: #3 lados iguales
        print("Es un triángulo equilatero")
    elif a == b or b == c or a == c: #2 lados iguales
            print("Es un triángulo isósceles")
    else:
            print("Es un triángulo escaleno")
else:
    print("El triángulo no se puede realizar")