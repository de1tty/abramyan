#Печёнкина Анастасия 17.09.2026  в 15:30
A = float(input('Введите значение A: '))
N = int(input('Введите значение N: '))
sum = 1
for i in range (1, N + 1):
    sum += A ** i
print(f'Сумма = {sum}')