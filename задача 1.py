from random import randint
n=int(input("Введите количество элементов массива: "))
a=[randint(-31,45) for i in range(n)]

print ( a [ i : i  +  10 ])
i = 0
while i < n:
    if a[i] < 0:
        del a[i]
        n -= 1
    else:
        i += 1

a.reverse()
print(a)
