#Печёнкина Анастасия 17.09.2026  в 15:36
N = int(input('Введите значение N: '))
N_factorial = 1
for i in range (1, N + 1):
    N_factorial *= i
print(f'Факториал числа {N} = {N_factorial}')