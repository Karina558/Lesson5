def odd_num (a, b):
    print(f'Непарні числа в діапазоні від {a} до {b}: ')
    for i in range(a, b + 1):
        if i % 2 != 0:
            print (i, end=' ')

odd_num(0, 105)