#Печёнкина Анастасия 17.09.2026  в 15:13
sum = 0
N = int(input('Введите значение для N: '))
if N <= 0:
    print('N должен быть больше 0')
else:
    for i in range(1, N, 2):
        sum += i
        print(sum)
N ** 2 == sum + (2 * N - 1)
a = N ** 2
print (a)