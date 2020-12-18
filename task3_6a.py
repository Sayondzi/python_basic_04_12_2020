"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(word):

    word1 = list(word.lower())
    word1_up = list(word.upper())
    word_new = word1.copy()
    word_new.pop(0)
    word_new.insert(0, word1_up[0])
    word_format = ''.join(word_new)
    return word_format

def int_words(text):
    len_list = len(text.split())
    idx = 0
    user_list = []
    while idx < len_list:
        user_text1 = text.split()[idx]
        user_list.append(int_func(user_text1))
        text_format1 = ' '.join(user_list)
        idx += 1
    return text_format1


user_text = input('Введите текст на английском языке.\nСлова вводить через пробелы.\nПосле завершения нажмите клавишу Enter.\n>>>')

print(int_words(user_text))

