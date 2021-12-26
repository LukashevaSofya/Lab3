from random import randint
a=[[randint(1, 10) for i in range(9)],
    [randint(1, 10) for i in range(9)],
    [randint(1, 10) for i in range(9)],
    [randint(1, 10) for i in range(9)],
    [randint(1, 10) for i in range(9)],
    [randint(1, 10) for i in range(9)],
    [randint(1, 10) for i in range(9)],
    [randint(1, 10) for i in range(9)],
    [randint(1, 10) for i in range(9)]]
print(a)

sum1=0

for i in range(0, 10):
    for j in range(0, 10):
        if j+1==10-i:
            for k in range(0, 10):
                sum1+=a #[k][j]
    for k1 in range(0, 10):
        sum1+=a #[i][k1]
        a[i][j]=sum1-a[i][j]
print(a)



