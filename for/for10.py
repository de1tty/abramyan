#Печёнкина Анастасия 16.09.2026 в 10:03
N = int(input('Введите число: '))
sum = 0
for i in range(1, N):
    sum += 1/i
print(f'Сумма чисел = {sum}')