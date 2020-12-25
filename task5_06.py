'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий по
этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее
количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
    Информатика: 100(л) 50(пр) 20(лаб).
    Физика: 30(л) — 10(лаб)
    Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

import os

file_path = os.path.join(os.path.dirname(__file__), 'annex06.txt')
book_table = {}
with open(file_path, 'r') as file:

    while True:
        content_line = file.readline()

        var = content_line.replace('.', '').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace('\n', '').split(' ')
        discipline = var[0].split(':')[0]
        book_table[discipline] = var[1:]
        if not content_line:
            break
new_book_table = book_table.copy()
print(new_book_table)
total = 0
book_final = {}
for key, value in new_book_table.items():
    for itm in value:
        if itm.isdigit():
            itm = int(itm)
            total += itm
    book_final[key] = total

print(book_final)