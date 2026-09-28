#Печёнкина Анастасия 17.09.2026  в 16:14
A = float(input('Введите значение A: '))
N = int(input('Введите значение N: '))
sum = 1
term = 1
for i in range (1, N + 1):
    term *= -A
    sum += term
print(f'значение выражения = {sum}')