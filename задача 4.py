
from random import randint
a = [] 
b = [] 
s = 0 
a1 = [] 
b1 = [] 
s1 = 0 
def sum(a,b,s): 
   
    a=[[randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)]]
    b=[[randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)]] 
    s=0 
    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
    for i in range(3): 
        for j in range(3): 
            c[i][j]=a[i][j]+b[i][j] 
            s+=c[i][j] 
    s=s/18 
    return c, s 
print('Сумма элементов массивов и их среднее значение',sum(a, b, s)) 
def raz(a,b,s1): 
    a1=[[randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)]]
    b1=[[randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)]] 
    s1=0 
    c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
    for i in range(3): 
        for j in range(3): 
            c[i][j]=a1[i][j]-b1[i][j] 
            s1+=a1[i][j]+b1[i][j] 
    s1=s1/18 
    return c,s1 
print('Разность элементов массива и их среднее значение',raz(a1, b1, s1))


