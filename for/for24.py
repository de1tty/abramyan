#Печёнкина Анастасия 18.09.2026 в 16:59
x = float(input('Введите значение x: '))
N = int(input('Введите значение N: '))
factorial = 1
sum = 1
sign = -1
for i in range(1, N + 1):
    w = i * 2
    factorial *= w
    c = sign * ((x ** w) / factorial)
    sum += c
    sign *= (-1)
print(f'значение выражения = {sum}')