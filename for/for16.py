#Печёнкина Анастасия 17.09.2026  в 15:28
A = float(input('Введите значение A: '))
N = int(input('Введите значение N: '))
for i in range(1, N + 1):
    sum = A ** i
    print(f'{A} в {i} степени = {sum}')