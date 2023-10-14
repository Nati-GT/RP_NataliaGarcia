def lectura():
    f=open("wcm.csv","r",encoding="utf8")
    line=f.readlines()
    listado=[]
    for  i in line:
        fila=i.rstrip('\n').split(',')
        listado.append(fila)
    # print(listado[0]) imprimir fila 0
    f.close()
    return(listado)
        

def subcampeon_mundial(listado):
    subcampeones={}
    for partidos in listado:
        if partidos[12]=='Final':
            if (partidos[2]>partidos[4])or(partidos[3]>partidos[5]):
                if partidos[1] not in subcampeones:
                    subcampeones[partidos[1]]=[partidos[16]]
                else:
                    list_year=subcampeones[partidos[1]]
                    list_year.append(partidos[16])
                    subcampeones[partidos[1]]=list_year                
            else:
                if partidos[0] not in subcampeones:
                    subcampeones[partidos[0]]=[partidos[16]]
                else:
                    list_year=subcampeones[partidos[0]]
                    list_year.append(partidos[16])
                    subcampeones[partidos[0]]=list_year
    subcampeones=dict(sorted(subcampeones.items()))
    print('\n---------------Listado de Subcampeones mundiales ----------------\n')
    for pais,year in subcampeones.items():
        print(f'{pais}: subcampeón en {year}')
    pais=input('Ingrese un pais: ')
    
    if pais in subcampeones:
        year=subcampeones[pais]
        print(f'fue campeon en los años {year}')
    else:
        print(f'{pais} no ha sido campeon del mundo')


def campeon_mundial(listado):
    campeones={}
    for partidos in listado:
        if partidos[12]=='Final':
            if (partidos[2]>partidos[4])or(partidos[3]>partidos[5]):
                if partidos[0] not in campeones:
                    campeones[partidos[0]]=[partidos[16]]
                else:
                    list_year=campeones[partidos[0]]
                    list_year.append(partidos[16])
                    campeones[partidos[0]]=list_year                
            else:
                if partidos[1] not in campeones:
                    campeones[partidos[1]]=[partidos[16]]
                else:
                    list_year=campeones[partidos[1]]
                    list_year.append(partidos[16])
                    campeones[partidos[1]]=list_year
    campeones=dict(sorted(campeones.items()))
    print('\n-------------------Listado de Campeones mundiales-------------------\n')
    for pais,year in campeones.items():
        print(f'{pais}: campeón en {year}')
    
    pais=input('Ingrese un pais: ')
    
    if pais in campeones:
        year=campeones[pais]
        print(f'fue campeon en los años {year}')
    else:
        print(f'{pais} no ha sido campeon del mundo')

def main():
    listado=lectura()
    while True:
        print('______________________Menu______________________\n\
    1.Cantidad de mundiales ganados por un pais\n\
    2.cantidad de subcampeonatos por un pais')
        Op=input('Ingrese alguna de las opciones anteriores: ')
        if (Op=="1"):
            campeon_mundial(listado)

        elif (Op=="2"):
            subcampeon_mundial(listado)

        elif (Op=="3"):
            pass

        elif (Op=="4") or (Op.lower()=="Salir" ):
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__=="__main__":
    main()
    