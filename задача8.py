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



 #2 var
    def determinant(matrix, mul):
    br = len(matrix)
    if br == 1:
        return mul * matrix[0][0]
    else:
        s = -1
        a = 0
        for i in range(br):
            m = []
            for j in range(1, br):
                buff = []
                for k in range(br):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            s *= -1
            a = a + mul * determinant(m, s * matrix[0][i])
    return a

print("Введите количество строк и столбцов в первом двумерном массиве(Через пробел): ")
n1, m1 = [int(i) for i in input().split()]
print("Записать элементы первого двумерного массива(Через пробел): ")
test_matrix = [[int(j) for j in input().split()] for i in range(n1)]
max_el1 = test_matrix[0][0]
print(determinant(test_matrix, 1))


