a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
sum = 0
for i in range(a, b + 1):
    sum += i
print(f'сумма чисел = {sum}')