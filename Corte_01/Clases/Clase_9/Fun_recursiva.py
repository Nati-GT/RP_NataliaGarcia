def cuenta_regresiva(num):
    num-=1
    if num>0:
        print(num)
        cuenta_regresiva(num)
    else:
        print('Booom')
    print('Fin de la funcion', num)
    
    
if __name__=="__main__":
    cuenta_regresiva(5)