class Articulo:
    def __init__(self, nombre, precio_sin_iva):
        self.nombre = nombre
        self.precio_sin_iva = precio_sin_iva
        self.precio_con_iva = self.calcular_precio_con_iva()

    def calcular_precio_con_iva(self):
        pass

class ArticuloCeroIVA(Articulo):
    def calcular_precio_con_iva(self):
        return self.precio_sin_iva

class ArticuloCincoIVA(Articulo):
    def calcular_precio_con_iva(self):
        return self.precio_sin_iva * 1.05

class ArticuloDiecinueveIVA(Articulo):
    def calcular_precio_con_iva(self):
        return self.precio_sin_iva * 1.19

def generar_articulos(lista_alimentos):
    articulos = []

    for nombre, precio, tipo_iva in lista_alimentos:
        if tipo_iva == 0:
            articulo = ArticuloCeroIVA(nombre, precio)
        elif tipo_iva == 5:
            articulo = ArticuloCincoIVA(nombre, precio)
        elif tipo_iva == 19:
            articulo = ArticuloDiecinueveIVA(nombre, precio)
        else:
            continue

        articulos.append(articulo)

    return articulos

def imprimir_producto(productos):
    for productos_iva in productos:
        for articulo in productos_iva:
            precio_sin_iva = round(articulo.precio_sin_iva, 2)
            precio_con_iva = round(articulo.precio_con_iva, 2)
            print(f"{articulo.nombre}: \n\
Precio sin IVA: {precio_sin_iva} \n\
Precio con IVA: {precio_con_iva}")

def main():
    alimentos_sin_iva = [
        ("Manzana", 10, 0),
        ("Pan", 5, 0),
        # Agrega más alimentos sin IVA si es necesario
    ]

    alimentos_con_iva_cinco = [
        ("Queso", 20, 5),
        ("Yogur", 15, 5),
        # Agrega más alimentos con IVA al 5% si es necesario
    ]

    alimentos_con_iva_diecinueve = [
        ("Carne", 30, 19),
        ("Pescado", 25, 19),
        # Agrega más alimentos con IVA al 19% si es necesario
    ]

    productos_sin_iva = generar_articulos(alimentos_sin_iva)
    productos_con_iva_cinco = generar_articulos(alimentos_con_iva_cinco)
    productos_con_iva_diecinueve = generar_articulos(alimentos_con_iva_diecinueve)

    print("Productos sin IVA:")
    imprimir_producto([productos_sin_iva])

    print("\nProductos con IVA al 5%:")
    imprimir_producto([productos_con_iva_cinco])

    print("\nProductos con IVA al 19%:")
    imprimir_producto([productos_con_iva_diecinueve])

if __name__ == "__main__":
    main()
