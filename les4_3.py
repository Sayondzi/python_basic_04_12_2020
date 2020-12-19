import sys

'''
from datetime import (datetime as dt,
                      timedelta as td,
                      )
'''
import datetime as dt
#from functools import reduce


date_str = '22.12.1987' # строка для запуска через RUN
#date_str = sys.argv[1] # строка для запуска через командную строку

b_date = dt.datetime.strptime(date_str, '%d.%m.%Y')
#now = dt.datetime.utcnow() - время по Гринвичу
now = dt.datetime.now()
#print(b_date)
#print(b_date.year)
#print(now.year-b_date.year)

#print(b_date.timestamp())
print(b_date.timestamp() * 1000)

delta = dt.timedelta(days=15)
new_date = now + delta
#print(b_date + delta)

#Различные способы вывода времени на экран
print('1)', new_date)
print('2)', new_date.time())
print('3)', new_date.strftime('%d-%m-%y %H:%M'))
print('4)', new_date.strftime('%d %B %y year, %H:%M'))
print('5)', new_date.strftime('%d %a %B %y year %D, %H:%M'))

int_date = 567118800000
print(dt.datetime.fromtimestamp(int_date / 1000))

'''
'0101010011111011101010'

четырёхбитная система:
'1111' == 15 
'0000' == 16   - при переходе от 15 к 16 наблюдается потеря одного бита информации

восьмибитная система
'00000000'
'01111111'
'10000000'  - получено при добавлении 1 к '011111111'

'''