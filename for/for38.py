#Печёнкина Анастасия 18.09.2026 в 20:01
N = int(input('Введите число N: '))
a = 0
sum = 0
for i in range(1, N + 1):
    b = i ** (N - a)
    sum += b
    a += 1
print(f'Сумма = {sum}')