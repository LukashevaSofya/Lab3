from random import randint
a=[randint(1, 10) for i in range(10)]
print(a)
#сумма итерационно
s=0
for i in a:
    s=s+i
print(s)
#сумма рекурсивно
def sum1(a):
    total = 0
    for element in a:
        if (type(element) == type([])):
            total = total + sum1(element)
        else:
            total = total + element
    return total
print(sum1(a))
#минимальное число итерационно
min1 = a[0]
for i in a:
    if i < min1:
        min1 = i
        
print(min1)
#минимальное число рекурсивно
def RecursiveMin(a):
    if len(a)==2:
        if a[0]<a[1]:
            return a[0]
        else:
            return a[1]
    else:
        X= RecursiveMin(a[1:])
        if a[0]<X:
            return a[0]
        else:
            return X
print(RecursiveMin(a))
