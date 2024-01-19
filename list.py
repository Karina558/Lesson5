user_text = input('Введіть речення або слово, щоб перевірити чи є воно паліндромом: ').replace(" ", "").lower().strip(' !.,')

if user_text == user_text[::-1]:
    print ('Ваше слово є паліндромом!')
else:
    print('Це слово не є паліндромом')