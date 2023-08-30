import math
import Fun_pro
def modulo(xo,yo,xf,yf):
    # Calcular las componentes rectangulares del vector
    xc=xf-xo
    yc=yf-yo

    #Calcular el módulo del vector utilizando el teorema de Pitágoras
    modulo=math.sqrt(xc**2 + yc**2)

    # Imprimir los resultados
    print("Las componentes rectangulares del vector son:")
    print("Componente x:", xc)
    print("Componente y:", yc)
    print("El módulo del vector es:", modulo)


if __name__=="__main__":
    modulo()