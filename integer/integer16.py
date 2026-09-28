#Печёнкина Анастасия 21.09.2026 в 20:30
A = int(input('Введите число: '))
c = A % 100
des = c // 10
sot = A // 100
edin = A % 10
print(str(sot) + str(edin) + str(des))