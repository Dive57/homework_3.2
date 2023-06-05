# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.


N = int(input('Кол. чисел:'))
a=[int(input('Ввести число:')) for i in range(N)]
x=int(input('Заданное число:'))
b=[abs(a[i]-x) for i in range(len(a))]
print(a[b.index(min(b))])