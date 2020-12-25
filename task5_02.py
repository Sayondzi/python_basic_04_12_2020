"""
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт количества строк, количества слов в каждой строке.
"""
import os

file_path = os.path.join(os.path.dirname(__file__), 'annex02.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    file_data = file.readlines()
    idx = 0
    print('#' * 60)
    if len(file_data) == 1:
        print(f'Файл содержит {len(file_data)} строку.')
    elif len(file_data) == 0 or len(file_data) >= 5:
        print(f'Файл содержит {len(file_data)} строк.')
    else:
        print(f'Файл содержит {len(file_data)} строки.')
    print('#' * 60)
    print('Построчное количество слов:')
    while idx < len(file_data):
        word_quantity = len(file_data[idx][:-1].split(' '))
        print(f'{idx + 1}-ая строка: {word_quantity}.')
        idx += 1
