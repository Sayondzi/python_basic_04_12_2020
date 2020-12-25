'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок
строк должен записываться в новый текстовый файл.
'''

import os

file_path = os.path.join(os.path.dirname(__file__), 'annex04.txt')
file_path_1 = os.path.join(os.path.dirname(__file__), 'annex04a.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    text_line = []
    while True:
        content_line = file.readline()
        text_line.append(content_line.replace('\ufeff', '').replace('\n', '').split(' '))
        if not content_line:
            break

new_text = text_line[:-1]


def translate(x, idx):
    text_translate = ['Раз', 'Два', 'Три', 'Четыре', '']
    x[0] = text_translate[idx]
    return x


with open(file_path_1, 'w', encoding='UTF-8') as file:
    idx = 0
    while idx < len(new_text):
        translate(new_text[idx], idx)
        file.write(' '.join(new_text[idx]))
        file.write('\n')
        print(' '.join(new_text[idx]))
        idx += 1
