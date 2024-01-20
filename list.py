import re
text = input('Введіть текст: ')
split = re.split(r'(?<=\.|\?|\!)\s', text)
cap = ''
for sentences in split:
    split = str(sentences.capitalize())
    cap += f'{split} '
print(cap)