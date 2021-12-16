
from random import randint
a = [[randint(1, 10) for i in range(9)],
     [randint(1, 10) for i in range(9)],
     [randint(1, 10) for i in range(9)]]
b = [[randint(1, 10) for i in range(9)],
     [randint(1, 10) for i in range(9)],
     [randint(1, 10) for i in range(9)]]

for i in range(9):
    s=0
    for j in range(9):
        s=s+a[i,j]+a[j,i]
        a[i,i]=s-a[i,i]
print(a,b) 
