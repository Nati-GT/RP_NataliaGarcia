print("Por favor ingrese 3 longitudes")
a = int(input(""))
b = int(input(""))
c = int(input(""))
if a - c < b < a + c or a - b < c < a + b or b - c < a < b + c:
    if a == b and  b == c: #3 lados iguales
        print("Es un triángulo equilatero")
    elif a == b and  b!=c or b == c and  c!=a or a == c: #2 lados iguales
        print("Es un triángulo isósceles")
    elif a!= c or b!= c and b!=a: #Ningun lado igual
        print("Es un triángulo escaleno")
else:
    print("El triángulo no se puede realizar")