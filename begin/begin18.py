#Печёнкина Анастасия 12.09.2026 в 19:20
A = float(input('Введите значение для точки A: '))
B = float(input('Введите значение для точки B: '))
C = float(input('Введите значение для точки C: '))
if (C > A and C < B and A < B) or (C < A and C > B and A > B):
    proizvedenie = abs(C - A) * abs(B - C)
    print('Произведение длин отрезков AC и BC = ', proizvedenie)
else:
    print('Точка C должна лежать между точками A и B')