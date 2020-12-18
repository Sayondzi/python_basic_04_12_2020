"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""

def int_func(text):
    text1 = list(text.lower())
    text1_up = list(text.upper())
    text_new = text1.copy()
    text_new.pop(0)
    text_new.insert(0, text1_up[0])
    text_format = ''.join(text_new)
    return text_format

user_text = input('Введите слово\n>>>')
print(int_func(user_text))
