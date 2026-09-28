#Печёнкина Анастасия 18.09.2026 в 17:40
x = float(input('Введите значение x: '))
N = int(input('Введите значение N: '))
sum = x
for i in range(1, N + 1):
    w = 2 * i - 1
    c = 2 * i + 1
    s = 2 * i
    y = (w * (x ** c)) / (s * c)
    sum += y
print(f'значение ввыражения = {sum}')