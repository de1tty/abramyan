#Печёнкина Анастасия 18.09.2026 в 20:01
N = int(input('Введите число N: '))
sum = 0
for i in range(1, N + 1):
    a = i ** i
    sum += a
print(f'Сумма = {sum}')