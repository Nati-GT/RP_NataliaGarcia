a=[1,2,3,4]
b=['uno','dos','tres','cuatro']
x=zip(a,b)
print(list(x))
m=list(x)
#print(m[0])

for i in range(len(m)):
    print(i)

for idx, valor in enumerate(m):
    print(idx)
    print(valor)
