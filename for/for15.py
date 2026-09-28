#Печёнкина Анастасия 17.09.2026  в 15:22
A = float(input('Введите значение A: '))
N = int(input('Введите значение N: '))
sum = 1
if N <= 0:
    print('N должен быть больше 0')
else:
    for i in range(1, N + 1):
        sum *= A
    print(f'{A} в степени {N} = {sum}')