# Создать список поездов. Структура словаря: номер
# поезда, пункт и время прибытия, пункт и время
# отбытия. Вывести все сведения о поездах, время
# пребывания в пути которых превышает 7 часов 20
# минут. (Примечание: использовать возможности
# библиотеки datetime).

import datetime

need_time = datetime.time(7, 30)
lsit_zap = []
list_rw = [{
     'train' : 'Andrew',
     'number' : 1584,
     'time' : datetime.time(7, 30)},
     {
     'train' : 'Stuwie',
     'number' : 1695,
     'time' : datetime.time(6, 15)},
     {
     'train' : 'Brandon',
     'number' : 1555,
     'time' : datetime.time(4, 30)},
     {
     'train' : 'Andrew',
     'number' : 1584,
     'time' : datetime.time(8, 30)}
     ]

for list in list_rw:
    if list_rw[list]['time'] > need_time:
        list_zap.append(list_rw())

print(list_zap)
