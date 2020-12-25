'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
'''

import os

file_path = os.path.join(os.path.dirname(__file__), 'annex03.txt')
print('Сотрудники, чей зароботок ниже 20 тыс. руб.:')
with open(file_path, 'r', encoding='UTF-8') as file:
    content_file = file.readlines()
    idx = 1
    k = 0
    pay_total = 0
    while idx < len(content_file):
        try:
            pay = float(content_file[idx].replace('\n', '').split(' ')[1])
            if pay < 20:
                k += 1
                print(k, content_file[idx].replace('\n', '').split(' ')[0])
            pay_total += pay
            idx += 1
        except ValueError as e:
            print('Ошибка во входящих данных.')
            break
    pay_mean = pay_total / (len(content_file) - 1)
    print(f'Средняя заработная плата сотрудников: {round(pay_mean, 2)} тыс. руб.')
