print('Seleccione el codigo a ejecutar: \n\
 1.Divisores \n 2.Producto \n 3.Fibbonacci')
Op=input('Ingrese alguna de las opciones anteriores: ')

if (Op=="1") or (Op.lower()=="Divisores" ):
    n=int(input("Ingrese un número: "))
    if n==0:
        print("Ningún número es divisible entre cero")
    else:
        print("Los divisores positivos de",n,"son: ")
        for i in range(1,n+1):
            if n%i == 0:
                print(i)
elif (Op=="2") or (Op.lower()=="Producto" ):
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    r=0
    if n2<0:
        n1,n2 = -n1,-n2
    for _ in range(n2):
        r+= n1
    print("El producto de", n1, "y", n2, "es:", r)
        
elif (Op=="3") or (Op.lower()=="Fibonacci" ):
    n=int(input("ingrese un numero "))
    s1=1
    s2=1
    s3=s1+s2
    print(str(s1)+","+str(s2),end=",")
    for i in range(1, n):
        i+=1
        s3=s1+s2
        s1=s2
        print(str(s3),end= ",")
        s2=s3
    # while(j<n):
    #     j+=1
    #     s3=s1+s2
    #     s1=s2
    #     print(str(s3),end= ",")
    #     s2=s3

else:
    print('Ingrese un termino valido')