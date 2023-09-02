def conteo(num):
    if num>0:
        conteo(num-1)
    print(num)
        
        
    
if __name__=="__main__":
    n=int(input('Hasta que numero desea contar: '))
    conteo(n)