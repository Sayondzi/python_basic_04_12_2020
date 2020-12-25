'''
Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.
'''
import os
from random import randint

def gen_list():
    lenght_origin_list = randint(5, 10)
    random_list = []
    idx = 0
    while idx < lenght_origin_list:
        random_list.append(randint(0,100))
        idx += 1
    return random_list

result_list = gen_list().copy()
print(f'Сгенерированная последовательность: {result_list}.')

file_path = os.path.join(os.path.dirname(__file__), 'annex05.txt')

total = 0
with open(file_path, 'w', encoding='UTF-8') as file:
    for el in result_list:
        file.write(f'{el} ')
        total += el
print('#' * 60)
print(f'Сумма чисел в файле annex05.txt: {total}.')
print('#' * 60)




