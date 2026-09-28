#Печёнкина Анастасия 20.09.2026 в 18:51
N = int(input('Введите первое число: '))
K = int(input('Введите второе число: '))
chastnoe = 0
if N < K:
    print('число N должно быть больше числа K')
else:
    while N >= K:
        N = N - K
        chastnoe += 1
    print(f'остаток = {N}, частное = {chastnoe}')