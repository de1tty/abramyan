a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
sum = 0
for i in range(a, b + 1):
    sum += i ** 2
print(f'сумма квадратов чисел = {sum}')