
from random import randint
n = 7
a = [[randint(1, 10) for j in range(n)] for i in range(n)]
print(a)
for col in zip(*a):
    print(*col[::-1])

