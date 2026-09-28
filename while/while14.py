#Печёнкина Анастасия 20.09.2026 в 20:42
A = int(input('Введите число: '))
sum = 0
K = 0
if A <= 1:
    print('ошибка')
else:
    while sum < A:
        K += 1
        sum += 1 / K
sum -= K
K -= 1
print(f'наименьшее число = {K}, сумма = {sum}')