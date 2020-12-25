"""
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем.
Об окончании вводы данных свидетельствует пустая строка.
"""
import os

file_path = os.path.join(os.path.dirname(__file__), 'annex01.txt')


try:
    with open(file_path, 'w', encoding='UTF-8') as file:
        while True:
            str_text = input('Введите текст:\n>>>')
            if str_text == '':
                break
            file.write(str_text + '\n')
except IOError:
    print('Произошла ошибка ввода-вывода.')

# проверка создданного файла и записей в нём.
with open(file_path, 'r', encoding='UTF-8') as file:
    file_data = file.read().split()
print(file_data)
