import math

def ingresar_coordenadas():
    x1=float(input("Ingresa la coordenada x del punto de origen: "))
    y1=float(input("Ingresa la coordenada y del punto de origen: "))
    x2=float(input("Ingresa la coordenada x del punto final: "))
    y2=float(input("Ingresa la coordenada y del punto final: "))
    return x1, y1, x2, y2

def calcular_modulo(x1, y1, x2, y2):
    modulo=math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return modulo

def calcular_componentes_rectangulares(x1, y1, x2, y2):
    componente_x=x2-x1
    componente_y=y2-y1
    return componente_x, componente_y

def main():
    print("Calculadora de módulo y componentes rectangulares de un vector")
    x1,y1,x2,y2=ingresar_coordenadas()
    
    modulo=calcular_modulo(x1, y1, x2, y2)
    componente_x, componente_y=calcular_componentes_rectangulares(x1, y1, x2, y2)
    
    print(f"El módulo del vector es: {round(modulo,2)}")
    print(f"Las componentes rectangulares del vector son:")
    print(f"Componente en x: {componente_x}")
    print(f"Componente en y: {componente_y}")

if __name__=="__main__":
    main()