#Печёнкина Анастасия 20.09.2026 в 21:56
N = int(input('Введите целое число: '))
c = 0
while N >= 1:
    i = N % 10
    N = N // 10
    if i == 2:
        c += i
if c >= 2:
    print('TRUE')
else:
    print('FALSE')