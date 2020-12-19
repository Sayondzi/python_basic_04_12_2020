"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(word: str):
    return ''.join((word[0].upper(), word[1:].lower())) if word else word

def int_words(text: str):
    return ' '.join(map(int_func, text.split(' ')))


user_text = input('Введите текст на английском языке.\nСлова вводить через пробелы.\nПосле завершения нажмите клавишу Enter.\n>>>')

print(int_words(user_text))

#assert int_func('маШина') == 'Машина', "int_func('маШина')"
#assert int_func('') == '', "int_func('')"
#assert int_func(' ') == ' ', "int_func(' ')"
#assert int_func('camal') == 'Camal', "int_func('camal')"