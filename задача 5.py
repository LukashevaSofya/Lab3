
from random import randint
A = [[randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)]]
B = [[randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)],
     [randint(1, 10) for i in range(3)]]

print(A, B)  
result = [] 
for i in range(len(A)):

    row = [] 
    for j in range(len(B)):

        product = 0 
        for v in range(len(A[i])):
            product += A[i][v] * B[v][j]
        row.append(product) 

    result.append(row) 


print(result)
