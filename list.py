try:
    input_list = input("Введіть список чисел через пробіл: ")
    user_list = list(map(int, input_list.split()))
    number_to_find = int(input("Введіть число, яке потрібно знайти: "))
    count = user_list.count(number_to_find)
    print(f"Число {number_to_find} зустрічається в списку {count} раз(ів).")
except Exception as e:
    print(e)