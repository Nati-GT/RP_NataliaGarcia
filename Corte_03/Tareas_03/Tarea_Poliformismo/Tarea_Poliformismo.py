import random

def lectura():
    f=open("Alimentos.txt", "r")
    lineas=f.readlines()
    f.close()
    listado=[]
    for linea in lineas[1:]:  # Ignorar la primera línea (encabezados)
        fila=linea.strip().split(',')
        if len(fila)==3:
            listado.append(fila)
    return listado

class Articulo:
    def __init__(self, nombre, precio_sin_iva):
        self._nombre=nombre
        self._precio_sin_iva=precio_sin_iva
        self._precio_con_iva=self.calcular_precio_con_iva()

    def set_nombre(self, nuevo_nombre):
        self._nombre=nuevo_nombre

    def set_precio_sin_iva(self, nuevo_precio_sin_iva):
        self._precio_sin_iva=nuevo_precio_sin_iva

    def set_precio_con_iva(self, nuevo_precio_con_iva):
        self._precio_con_iva=nuevo_precio_con_iva

    def get_nombre(self):
        return self._nombre

    def get_precio_sin_iva(self):
        return self._precio_sin_iva

    def get_precio_con_iva(self):
        return self._precio_con_iva

    def calcular_precio_con_iva(self):
        pass

class ArticuloCeroIVA(Articulo):
    def __init__(self, nombre, precio_sin_iva):
        super().__init__(nombre, precio_sin_iva)

    def calcular_precio_con_iva(self):
        return self.get_precio_sin_iva()

class ArticuloCincoIVA(Articulo):
    def __init__(self, nombre, precio_sin_iva):
        super().__init__(nombre, precio_sin_iva)

    def calcular_precio_con_iva(self):
        return self.get_precio_sin_iva()*1.05

class ArticuloDiecinueveIVA(Articulo):
    def __init__(self, nombre, precio_sin_iva):
        super().__init__(nombre, precio_sin_iva)

    def calcular_precio_con_iva(self):
        return self.get_precio_sin_iva()*1.19

def asignar_productos_iva(alimentos):
    productos_cero_iva=[]
    productos_cinco_iva=[]
    productos_diecinueve_iva=[]

    for item in alimentos:
        descripcion=item[1]
        precio_sin_iva=random.randint(1,10000)  # Precio aleatorio sin IVA entre 1 y 100

        if float(item[2])==0:
            producto=ArticuloCeroIVA(descripcion, precio_sin_iva)
            productos_cero_iva.append(producto)
        elif float(item[2])==0.05:
            producto=ArticuloCincoIVA(descripcion, precio_sin_iva)
            productos_cinco_iva.append(producto)
        elif float(item[2])==0.19:
            producto=ArticuloDiecinueveIVA(descripcion, precio_sin_iva)
            productos_diecinueve_iva.append(producto)

    return productos_cero_iva, productos_cinco_iva, productos_diecinueve_iva

def mostrar_productos_iva(productos):
    for lista_productos in productos:
        for producto in lista_productos:
            precio_sin_iva=round(producto.get_precio_sin_iva(), 2)
            precio_con_iva=round(producto.get_precio_con_iva(), 2)
            print(f"{producto.get_nombre()}: \n\
Precio sin IVA: {precio_sin_iva} \n\
Precio con IVA: {precio_con_iva}")
def main():
    alimentos=lectura()

    productos_cero_iva, productos_cinco_iva, productos_diecinueve_iva = asignar_productos_iva(alimentos)

    print("------------Productos con IVA al 0%:------------")
    mostrar_productos_iva([productos_cero_iva])

    print("\n------------Productos con IVA al 5%:------------")
    mostrar_productos_iva([productos_cinco_iva])

    print("\n------------Productos con IVA al 19%:------------")
    mostrar_productos_iva([productos_diecinueve_iva])

if __name__ == "__main__":
    main()
