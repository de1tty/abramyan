#Печёнкина Анастасия 20.09.2026 в 18:57
N = int(input('Введите число: '))
current = 1
if N < 1:
    print('ошибка')
else:
    while current < N:
        current *= 3
    if current == N:
        print('TRUE')
    else:
        print('FALSE')