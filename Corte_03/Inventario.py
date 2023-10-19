def crear_inventario(lista):
    inventario={}
    for elemento in lista:
        if elemento not in inventario:
            inventario[elemento]=1
        else:
            inventario[elemento]+=1
    print(inventario)
def agregar_elementos(inv,nuevos):
    nuevos=crear_inventarios
def main():
    crear_inventario(['carbon','madera'])

if __name__=="__main__":
    main()
