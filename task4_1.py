'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника.
В расчете необходимо использовать формулу:
    (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с
параметрами.
'''

from sys import argv
from task4_1a import my_wages

if len(argv) != 4:
    print('Ошибка ввода параметров.')
    exit()

variables = []
for param in argv[1:]:
    try:
        param = float(param)
        variables.append(param)
    except ValueError as e:
        print(f'{e}\nВведены неверные значения.')
        exit()
        break

print(my_wages(*variables))
