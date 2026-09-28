#Печёнкина Анастасия 20.09.2026 в 22:35
N = int(input('Введите число: '))
F1 = 1
F2 = 1
while F2 < N:
    F1, F2, = F2, F1 + F2
    print(F2)
if F2 == N:
    print("TRUE")
else:
    print("FALSE")