#Печёнкина Анастасия 20.09.2026 в 19:13
N = int(input('Введите число: '))
double_factorial = 1
num = 2
if N < 1:
    print('ошибка')
else:
    while N >= 1:
        double_factorial *= N
        N = N - num
        num += 2
    print(f'двойной факториал = {double_factorial}')