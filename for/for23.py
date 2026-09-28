#Печёнкина Анастасия 17.09.2026  в 16:35
x = float(input('Введите значение x: '))
N = int(input('Введите значение N: '))
sum = x
term = x
factorial = 1
sign = 1
for i in range (1, N + 1):
    w = 2 * i + 1
    factorial *= w
    c = sign * (x ** w / factorial)
    sum += c
    sign *= (-1)
print(f'Сумма = {sum}')