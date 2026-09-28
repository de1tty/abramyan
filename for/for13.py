#Печёнкина Анастасия 16.09.2026 в 10:26
N = int(input('Введи количество слагаемых: '))
sum = 0
for i in range(1, N + 1):
    sum = sum + ((i / 10) + 1)
    sign = (-1) ** (i + 1)
    total = sum * sign
print(f'сумма = {total}')