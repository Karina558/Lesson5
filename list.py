def odd_num (a, b):
    for i in range(a, b + 1):
        if i % 2 != 0:
            print (i, end=' ')

a = int(input('Введіть перше число діапазону: '))
b = int(input('Введіть друге число діапазону: '))

print(f'Непарні числа в діапазоні від {a} до {b}: ', end=''), odd_num(a, b)