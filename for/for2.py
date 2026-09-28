a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
n = 0
for i in range (a, b + 1):
    print(i, end=" ")
    n += 1
print(f'количество чисел = {n}')