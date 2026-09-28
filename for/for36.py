#Печёнкина Анастасия 18.09.2026 в 19:59
N = int(input('Введите число N: '))
K = int(input('Введите число K: '))
sum = 0
for i in range(1, N + 1):
    a = i ** K
    sum += a
print(f'Сумма = {sum}')