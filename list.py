import re
text = input('Введіть текст: ')

#розділяється текст на окремі речення за допомогою регулярних виразів:
split = re.split(r'(?<=\.|\?|\!)\s', text)

cap = ''
for sentences in split:
    split = str(sentences.capitalize())
    cap += f'{split} '
print(cap)

count_num = 0
count_punctuation = 0
for i in text:
    if i.isdigit():
        count_num += 1
    elif not i.isspace() and not i.isalnum():
        count_punctuation += 1
    else:
        pass

exclamation = re.findall('!', text)
count_excl = len(exclamation)

print('У вашому тексті:\n - кількість цифр: ', count_num)
print(' - кількість розділових знаків: ', count_punctuation)
print(' - кількість окличних знаків: ', count_excl)
