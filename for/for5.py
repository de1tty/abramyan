num = 0.1
a = int(input('укажите стоимость конфет за 1 кг: '))
for i in range(0, 10):
    b = a * num
    print(f'цена за {round(num, 2)} кг = {round(b, 2)}')
    num += 0.1