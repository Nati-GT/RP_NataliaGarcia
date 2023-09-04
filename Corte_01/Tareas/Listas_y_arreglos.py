import random

def generar_numeros_aleatorios():
    numeros=[]
    for _ in range(15):
        numero=random.randint(1, 100)
        numeros.append(numero)
    return numeros

def ordenar_lista(numeros):
    numeros.sort()
    return numeros

def obtener_dias_mes():
    meses= {
        'enero': (31,'el 8 de enero','Año Nuevo'),
        'febrero': (28,'el 14 de febrero','Día de San Valentín'),
        'marzo': (31,'el 20 de marzo','Día de San José'),
        'abril':(30,'el 30 de abril','Dia del niño'),
        'mayo':(31,'el 8 de mayo','Dia de la madre'),
        'junio':(30,'el 16 de junio','Dia del padre'),
        'julio':(31,'el 20 de julio','Dia de la idependencia'),
        'agosto':(31,'el 7 de agosto','Batalla de Boyaca'),
        'septiembre':(30,'el 16 de septiembre','amor y amistad'),
        'octubre':(31,'el 31 de octubre','Halloween'),
        'noviembre':(30,'el 23 de noviembre','Accion y Gracias'),
        'diciembre':(31,'el 25 de diciembre','Navidad')}
    nombre_mes=input("Ingresa el nombre de un mes del año: ").lower()
    if nombre_mes in meses:
        dias,festivo,celebracion=meses[nombre_mes]
        print("El mes de",nombre_mes,"tiene",dias,"días y su festivo es",festivo, celebracion)
    else:
        print("Mes inválido.")

def almacenar_numeros():
    numeros= []
    while True:
        numero=int(input("Ingrese un número (y para salir ingrese un número negativo): "))
        if numero<0:
            break
        numeros.append(numero)
    return numeros

def eliminar_duplicados(numeros):
    numeros_sin_duplicados=list(set(numeros))
    return numeros_sin_duplicados

def main():
    while True:
        print('Seleccione el codigo a ejecutar: \n\
  1.Generar y ordenar números aleatorios \n\
  2.Obtener días y festivos de un mes \n\
  3.Almacenar números y eliminar duplicados \n\
  4.Salir')
        opcion=input('Ingrese alguna de las opciones anteriores: ')
        if opcion=="1":
            numeros_aleatorios=generar_numeros_aleatorios()
            numeros_ordenados=ordenar_lista(numeros_aleatorios)
            print("Números generados aleatoriamente:", numeros_aleatorios)
            print("Números ordenados:", numeros_ordenados)
        elif opcion=="2":
            obtener_dias_mes()
        elif opcion=="3":
            numeros=almacenar_numeros()
            print("Lista original:", numeros)
            numeros_sin_duplicados=eliminar_duplicados(numeros)
            print("Lista sin duplicados:", numeros_sin_duplicados)
        elif opcion=="4":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__=="__main__":
    main()
