class Producto:
    def __init__(self, nombre, precio, cantidad_disponible=0):
        self.__nombre=nombre
        self.__precio=precio
        self.__cantidad_disponible=cantidad_disponible

    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre

    def setPrecio(self, precio):
        self.__precio=precio

    def getPrecio(self):
        return self.__precio

    def setCantidadDisponible(self, cantidad_disponible):
        self.__cantidad_disponible=cantidad_disponible

    def getCantidadDisponible(self):
        return self.__cantidad_disponible
    
    def obtener_info(self):
        return f"Nombre: {self.getNombre()} \n\
Precio: {self.getPrecio()} \n\
Cantidad disponible: {self.getCantidadDisponible()}"

    def restar_cantidad(self):
        self.__cantidad_disponible-=1

    def verificar_disponibilidad(self):
        return self.__cantidad_disponible>0


class Snack(Producto):
    def __init__(self, nombre, precio, cantidad_disponible, tipo_snack):
        super().__init__(nombre, precio, cantidad_disponible)
        self.__tipo_snack=tipo_snack

    def setTipoSnack(self, tipo_snack):
        self.__tipo_snack=tipo_snack

    def getTipoSnack(self):
        return self.__tipo_snack

    def obtener_info(self):
        return f"{super().obtener_info()} \nTipo de snack: {self.getTipoSnack()}"


class Bebida(Producto):
    def __init__(self, nombre, precio, cantidad_disponible, tamano_bebida):
        super().__init__(nombre, precio, cantidad_disponible)
        self.__tamano_bebida=tamano_bebida

    def setTamanoBebida(self, tamano_bebida):
        self.__tamano_bebida=tamano_bebida

    def getTamanoBebida(self):
        return self.__tamano_bebida
    
    def obtener_info(self):
        return f"{super().obtener_info()} \n\
        Tamaño de la bebida: {self.getTamanoBebida()}"


class MaquinaDispensadora:
    def __init__(self):
        self.productos=[]

    def agregar_productos(self, producto):
        self.productos.append(producto)

    def realizar_venta(self, producto):
        if producto.verificar_disponibilidad():
            producto.restar_cantidad()
            return f"Venta realizada. {producto.getNombre()} cuesta {producto.getPrecio()}."
        else:
            return "Lo siento, el producto no está disponible."

    def total_ventas(self):
        return sum([producto.getPrecio() for producto in self.productos])


def main():
    maquina=MaquinaDispensadora()
    agregar_mas=True

    while agregar_mas:
        tipo_producto=input("¿Qué tipo de producto desea agregar? (Producto/Snack/Bebida): ").capitalize()

        if tipo_producto=="Producto":
            nombre_producto=input("Ingrese el nombre del producto: ")
            precio_producto=float(input("Ingrese el precio del producto: "))
            cantidad_producto=int(input("Ingrese la cantidad disponible del producto: "))

            producto=Producto(nombre_producto, precio_producto, cantidad_producto)
            maquina.agregar_productos(producto)
        elif tipo_producto=="Snack":
            nombre_snack=input("Ingrese el nombre del snack: ")
            precio_snack=float(input("Ingrese el precio del snack: "))
            cantidad_snack=int(input("Ingrese la cantidad disponible del snack: "))
            tipo_snack=input("Ingrese el tipo de snack: ")

            snack=Snack(nombre_snack, precio_snack, cantidad_snack, tipo_snack)
            maquina.agregar_productos(snack)
        elif tipo_producto=="Bebida":
            nombre_bebida=input("Ingrese el nombre de la bebida: ")
            precio_bebida=float(input("Ingrese el precio de la bebida: "))
            cantidad_bebida=int(input("Ingrese la cantidad disponible de la bebida: "))
            tamano_bebida=input("Ingrese el tamaño de la bebida: ")

            bebida=Bebida(nombre_bebida, precio_bebida, cantidad_bebida, tamano_bebida)
            maquina.agregar_productos(bebida)
        else:
            print("Tipo de producto no válido.")

        decision=input("¿Desea agregar otro producto? (Sí/No): ").capitalize()
        if decision!="Si" and decision !="Sí":
            agregar_mas=False

    
    print("\nRealizando algunas ventas:")
    for producto in maquina.productos:
        print(maquina.realizar_venta(producto))
    
    print(f"\nTotal de ventas: {maquina.total_ventas()}")

if __name__=="__main__":
    main()


