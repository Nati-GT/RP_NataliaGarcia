from factorial import factorial as f
def main():
    n=int(input('ingrese la cantidad de elementos: '))
    m=int(input('ingreese de a cuantos los quiere agrupar: '))
    
    cb=(f(n)/(f(m)*(f(n-m))))
    print(f'El numero de combinaciones posibles es {cb}')
    

if __name__=="__main__":
    main()
    