from random import randint
a=[randint(1, 100) for i in range(10)]
print(a)
c= [ n for n in a if n%2 ]
b=c[::2]
print(max(b))
