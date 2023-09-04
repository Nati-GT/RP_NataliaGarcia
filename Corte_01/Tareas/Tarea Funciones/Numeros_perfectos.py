
def calcular_divisores(numero):
    divisores=[]
    for i in range(1,numero):
        if numero%i==0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(numero):
    suma_divisores=sum(calcular_divisores(numero))
    return suma_divisores==numero

def imprimir_numeros_perfectos(cantidad):
    numeros_perfectos=[]
    numero=1
    while len(numeros_perfectos)<cantidad:
        if es_numero_perfecto(numero):
            numeros_perfectos.append(numero)
        numero+=1

    print(f"Los {cantidad} primeros números perfectos son:")
    for numero in numeros_perfectos:
        print(numero)

# Solicitar la cantidad de números perfectos a imprimir
cantidad=int(input("Ingrese la cantidad de números perfectos a imprimir (máximo 4): "))

# Validar la cantidad ingresada
if cantidad>4:
    cantidad=4

# # Imprimir los números perfectos
imprimir_numeros_perfectos(cantidad)

