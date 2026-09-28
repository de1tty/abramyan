#Печёнкина Анастасия 22.09.2026 17:50
K = int(input('Введите номер дня: '))
if K % 7 == 4: #вс
    print(0)
if K % 7 == 5: #пн
    print(1)
if K % 7 == 6: #вт
    print(2)
if K % 7 == 0: #ср
    print(3)
if K % 7 == 1: #чт
    print(4)
if K % 7 == 2: #пт
    print(5)
if K % 7 == 3: #сб
    print(6)