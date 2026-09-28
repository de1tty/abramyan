#Печёнкина Анастасия 20.09.2026 в 22:19
import math

N = int(input('Введите число: '))
L = []
for x in range(2,N+1):
    n = math.sqrt(x)
    i = 2
    k = 0
    while i <= n:
        if int(x / i)*i == x:
            k += 1
            break
        i += 1
    if k == 0:
        L.append(x)
print(L)