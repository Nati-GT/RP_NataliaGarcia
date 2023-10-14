def lectura():
    f=open("Alimentos.txt", "r")
    lineas=f.readlines()
    f.close()
    listado=[]
    for linea in lineas:
        fila=linea.strip().split(',')
        if len(fila)==3:
            listado.append(fila)
    return listado

def menu(alimentos):
    print("Código → Producto")
    for fila in alimentos:
        codigo,producto=fila[0], fila[1]
        print(f"{codigo} → {producto}")

def total(codigo,precio,alimentos):
    for fila in alimentos:
        if codigo==fila[0]:
            descripcion=fila[1]
            tarifa_iva=float(fila[2])
            iva=round(precio*tarifa_iva,2)
            precio_total=round(precio+iva,2)
            return descripcion, precio, tarifa_iva, iva, precio_total
    return None, None, None, None, None #Esto indica que no se encontró el producto y que no hay valores válidos para descripción, precio, tasa de IVA, IVA y precio total.

def main():
    alimentos=lectura()
    factura=[]

    while True:
        menu(alimentos)
        codigo=input("Ingrese el código del producto (o 'salir' para finalizar): ")
        if codigo.lower()=='salir':
            break
        
        precio=float(input("Ingrese el precio que desea asignar: "))
        nombre_producto, precio_unitario, tarifa_iva, iva, precio_total=total(codigo, precio, alimentos)

        if nombre_producto is not None:
            print(f"\nProducto: {nombre_producto}")
            print(f"Precio Unitario: {precio_unitario}")
            print(f"Tasa de IVA: {tarifa_iva}")
            print(f"IVA: {iva}")
            print(f"Precio Total: {precio_total}\n")

            factura.append({
                "Producto":nombre_producto,
                "Precio Unitario":precio_unitario,
                "Tasa de IVA":tarifa_iva,
                "IVA":iva,
                "Precio Total":precio_total
            })
        else:
            print(f"No se encontró ningún producto con el código '{codigo}'")

    # Generar factura (Trate de acomodarla para que se viera bonita pero no pude profe :c )
    print("\n-------------------- Factura --------------------")
    print("ProductoPrecio   Unitario    Tasa de IVA     IVA     Precio Total")
    total_factura=0
    for pro in factura:
        total_factura+=pro["Precio Total"]
        print(f"{pro['Producto']}  / {pro['Precio Unitario']}  /  {pro['Tasa de IVA']}  /  {pro['IVA']}  /  {pro['Precio Total']}")
    print(f"Total Factura: {total_factura}")

if __name__=="__main__":
    main()
