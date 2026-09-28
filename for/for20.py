#Печёнкина Анастасия 17.09.2026  в 15:36
N = int(input('Введите значение N: '))
sum = 0
factorial = 1
for i in range (1, N + 1):
    factorial *= i
    sum += factorial
print(f'Сумма факториалов от 1 до {N} = {sum}')