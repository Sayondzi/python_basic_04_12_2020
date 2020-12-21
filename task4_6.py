'''
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
'''
from itertools import count

print('#' * 80)
print('Итератор, генерирующий целые числа, начиная с указанного.')
print('#' * 80)

user_var = int(input('Укажите начальное число:\n>>>'))
for el in count(user_var):
    if el > user_var + 7:
        break
    else:
        print(el)


print('#' * 80)
print('Итератор, повторяющий элементы некоторого списка, определенного заранее.')
print('#' * 80)
from itertools import cycle
from random import randint
from random import choice

lenght_origin_list = randint(3, 5)  # Определяем случайную длину слписка в интервале от 4 до 6 элементов.

random_list = []
alphabet = (
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z')

i = 0
while i < lenght_origin_list:
   # random_list.append(alphabet[randint(0, 25)])
    random_list.append(choice(alphabet))
    i += 1
print('Исходный список: ', random_list)

c = 0

for el in cycle(random_list):
    if c > 12:
        break
    print(el)
    c += 1
