try:
    text = input('Введіть текст: ').lower()
    words_to_replace = input("Введіть слова, які потрібно замінити в тексті : ").split()
    for word in words_to_replace:
        text = text.replace(word, word.upper())
    print(text)
except Exception as a:
    print (a)

