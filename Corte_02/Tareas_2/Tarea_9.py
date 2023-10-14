from random import randint as r

def crear_matriz():
    matriz=[]
    for i in range(5):
        matriz.append([])
        for j in range(10):
            num=r(1,100)
            matriz[i].append(num)
    return matriz
    
def imprimir_matriz(matriz):
    for i in matriz:
        print(i)

def valor_mayor(matriz):
    n_max=matriz[0][0]
    posicion_mayor=(0,0)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]>n_max:
                n_max=matriz[i][j]
                posicion_mayor=(i,j)
    return posicion_mayor, n_max
                
def valor_menor(matriz):
    n_min=matriz[0][0]
    posicion_menor=(0, 0)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]<n_min:
                n_min=matriz[i][j]
                posicion_menor=(i,j)
    return posicion_menor, n_min
            
def organizar_matriz(matriz):
    matriz_final= []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_final.append(matriz[i][j])
            matriz_final.sort(reverse=True)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j]=matriz_final.pop(0)
        print(matriz[i])

def posiciones(palabra,letra):
    pos=[]
    for i in range(len(palabra)):
        if palabra[i]==letra:
            pos.append(i)
    return pos

def encontrar(lista):
    if len(lista)==1:
        return lista[0]
    mayor=lista[0]
    for i in lista:
        if i>mayor:
            mayor=i
    return mayor

def main():
    while True:
        print('Seleccione el codigo a ejecutar: \n\
  1.Matriz ordenada \n\
  2.Elemento mayor \n\
  3.lista de string \n\
  4.Salir')
        Op=input('Ingrese alguna de las opciones anteriores: ')
        if (Op=="1") or (Op.lower()=="matriz ordenada" ):
            print('-----------------La matriz generada es:-----------------')
            matriz=crear_matriz()
            imprimir_matriz(matriz)
            posicion_mayor, n_max=valor_mayor(matriz)
            posicion_menor, n_min=valor_menor(matriz)
            
            print(f'el valor mayor en esta matriz es {n_max} y esta ubicado en la posicion {posicion_mayor}.\n\
el valor menor en esta matriz es {n_min} y esta ubicado en la posicion {posicion_menor}.\n\
-----------------La matriz organizada de mayor a menor es:-----------------')
            organizar_matriz(matriz)

        elif (Op=="2") or (Op.lower()=="Elemento mayor" ):
            Lista=[r(1, 30) for _ in range(15)]
            maximo_lista=encontrar(Lista)
            print("La lista generada aleatoreamente es:",Lista)
            print("Y el numero maximo es:", maximo_lista)

        elif (Op=="3") or (Op.lower()=="lista de string" ):
            palabra=str(input('Ingrese una palabra: '))
            letra=str(input('Ingrese una letra de esa palabra: '))
            pos=posiciones(palabra,letra)
            if not pos:
                print(f"la letra '{letra}' no se encuentra en la palabra '{palabra}'")
            else:
                print(f"Las posiciones de '{letra}' en '{palabra}' son: {pos}")
            
        elif (Op=="4") or (Op.lower()=="Salir" ):
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

    
if __name__=="__main__":
    main()
