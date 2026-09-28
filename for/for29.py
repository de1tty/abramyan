#Печёнкина Анастасия 18.09.2026 в 17:58
N = int(input('Введите значение N: '))
A = float(input('Введите значение первой точки: '))
B = float(input('Введите значение второй точки: '))
num = 1
if A > B or N < 1:
    print('ошибка')
else:
    for i in range(1, int(B + 1)):
        H = (B - A) / N
        otrezok = A + H * i
        print(f'длина {num} отрезка = {otrezok}')
        num += 1
print(f'длина каждого отрезка = {H}')