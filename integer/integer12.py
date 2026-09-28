#Печёнкина Анастасия 21.09.2026 в 19:42
A = int(input('Введите число: '))
vtoroe = A // 10
desyatki = vtoroe % 10
edinica = A % 10
sotni = A // 100
print(str(edinica) + str(desyatki) + str(sotni))