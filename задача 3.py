
def func(l, n):
    return l[n:] + l[:n]
try:
    s=input('Введите список чисел через пробел: ')
    l = list(map(int, s.split()))
    if l == []:
        print('Пусто')
    else:
        
        n = int(input('На сколько сдвиг? - '))
        while len(l)<n:
            n-=len(l)
        print(func(l,n))
        
except:
    print('Что-то не так')

