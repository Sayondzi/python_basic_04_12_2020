"""
Неизменяемые типы (можно переназначить)
int - целые числа
float - десятичные числа (с разделителем - точка)
bool

None

str - строка
tuple - кортеж
frozenset

Изменяемые типы
list - список

dict - словарь
set - множество



"""


"""
a = float('inf') - бесконечность
а = float('nan') - число, которое не число
sqrt - извлечение корня

магия с числами
    a = 22
    b = 22
    id(a) == id(b)
но
    a = 258
    b = 258
    id(a) != id(b)
и так
    a = 300
    b = a
    a == b
    id(a) == id(b)
магия со строками
    a = 'hello'
    b = 'hello'
    a is b -> True
    
    a = 'Приветы'
    b = 'Приветы'
    a is b -> False (т.к. не на латинице)

a[start: stop: step:]
Приветы Приветы
-8 -7 -6 -5 -4 -3 -2 -1     0 1 2 3 4 5 6 7

 Строка
some = 'gerlglegjbrtjdfhdfhdfghghdnmjgndgfdfgleg'

for item in some:
    print(item)

idx = 0
while idx < len(some):
    item = some[idx]
    print(item)
    idx += 1

idx = 0
while idx < len(some):
    item = some[idx:idx+2]
    print(item)
    idx += 2

 У строк есть метод split для разделения строки на составляющие
 some.split('') - в кавычках указывается разделитель слов в строке
ome_list = [1, 2, 3, 'some string', True, 22.3 ]
 Списки
 d = c[:] - срез, копирование списка с новым ID
 a.append(4) - в конце списка появится новый элемент '4'
 a.append(a) список можно вложить самого в себя

 Кортежи
 tuple -  обладает всеми свойствами списка, но изменить его нельзя.
 Пример записи:
 a = 1, 2, 3, 4, 5, 6
 a, b = (1, 2)

Словари

some_dict = {
    'one': 1643,
    'two': 46534,
    'user_name': 'Some name',
    'user_age': 22,
}


 по ключу определяется значение


Множество

some_set = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 'some'}
во множество нельзя добавить список

some_set.difference(some_set2) - показывает отличие множеств
some_set.intersection(some_set2) - показывает схожесть множеств (в некоторых частных случаях зависит от от последовательности данных)
some_set & some_set2 - - показывает схожесть множеств (постоянный результат)
some_set.intersection(some_set2) == some_set & some_set2
some_set | some_set2 - объединение
some_set.add(34344) - добавление данных (34344) в массив
some_set.pop() - удаление данных из массива

frozenset - неизменяемое множество


"""