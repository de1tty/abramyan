#Печёнкина Анастасия 17.09.2026  в 16:23
x = float(input('Введите значение x: '))
N = int(input('Введите значение N: '))
sum = 1
factorial = 1
for i in range (1, N + 1):
    factorial *= i
    znachenie = (x ** i) / factorial
    sum += znachenie
print(f'Сумма = {sum}')