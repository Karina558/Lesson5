user_text = input('Введіть речення або слово, щоб перевірити чи є воно паліндромом: ').replace(" ", "").lower().strip(' !.,')
check = user_text[::-1]

if user_text == check:
    print ('Ваше слово є паліндромом!')
else:
    print('Це слово не є паліндромом')