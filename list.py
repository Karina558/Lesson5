import re

text = input('Введіть текст: ')
sentences = re.split(r'[.!?]+\s|\.\.\.|\!\!\!|\!\?|\?\!', text)
sentences = [sentences.strip() for sentences in sentences if sentences.strip()]
number_of_sentences = len(sentences)

print(f'Кількість речень: {number_of_sentences}')
