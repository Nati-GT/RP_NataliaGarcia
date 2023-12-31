def crear_inventario(lista):
    inventario={}
    for elemento in lista:
        if elemento not in inventario:
            inventario[elemento]=1
        else:
            inventario[elemento]+=1
    return inventario

def agregar_elementos(inv,nuevos):
    nuevos=crear_inventario(nuevos)
    for elemento in nuevos:
        if elemento not in inv:
            inv[elemento]=nuevos[elemento]
        else:
            inv[elemento]+=nuevos[elemento]
    return inv

def reducir_inventario(inv,nuevos):
    nuevos=crear_inventario(nuevos)
    for elemento in nuevos:
        if elemento not in inv:
            inv[elemento]=nuevos[elemento]
        else:
            if(inv[elemento]-nuevos[elemento])<0:
                inv[elemento]=0
            else:
                inv[elemento]-=nuevos[elemento]
    return inv
    
def borrado_inventario(inv,item):
    if item in inv:
        inv.pop(item)
        #del inv[item]
        print(inv)
    else:
        print('El item no esta en el inventario')

def main():
    crear_inventario(['carbon','madera','madera',\
        'diamante','diamante','diamante','carbon',\
            'hierro'])
    agregar_elementos({'madera':1},['madera','hierro','madera','carbon'])
    reducir_inventario({'carbon':2,'hierro':1,'diamante':0},['diamante','carbon','hierro','hierro'])
    borrado_inventario({'carbon':2,'madera':1,'diamante':1},'diamante')

if __name__=="__main__":
    main()