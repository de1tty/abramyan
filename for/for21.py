#Печёнкина Анастасия 17.09.2026  в 16:17
N = int(input('Введите значение N: '))
sum = 1
factorial = 1
for i in range (1, N + 1):
    factorial *= i
    a = 1/i
    sum += a
print(f'Сумма = {sum}')