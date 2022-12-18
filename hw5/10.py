# Создать список поездов. Структура словаря: номер
# поезда, пункт и время прибытия, пункт и время
# отбытия. Вывести все сведения о поездах, время
# пребывания в пути которых превышает 7 часов 20
# минут. (Примечание: использовать возможности
# библиотеки datetime).

from datetime import datetime
new_list = []
list_rw = [{
     'number' : 1584,
     'from' : 'Minsk',
     'to' : 'Berlin',
     'departure' : datetime(2021, 1, 7, 12, 30, 40),
     'arrival' : datetime(2021, 1, 8, 11, 22, 35)
     },
     {
     'train' : 'Stuwie',
     'number' : 1695,
     'from' : 'Minsk',
     'to' : 'Brest',
     'departure' : datetime(2021, 1, 7, 10, 15, 14),
     'arrival' : datetime(2021, 1, 7, 14, 17, 32)
     },
     {
     'train' : 'Brandon',
     'number' : 1555,
     'from' : 'Minsk',
     'to' : 'Kiev',
     'departure' : datetime(2021, 1, 6, 19, 26, 16),
     'arrival' : datetime(2021, 1, 7, 10, 55, 16)
     },
     {
     'train' : 'Andrew',
     'number' : 1584,
     'from' : 'Minsk',
     'to' : 'Ghomel',
     'departure' : datetime(2021, 1, 5, 10, 44, 17),
     'arrival' : datetime(2021, 1, 5, 14, 13, 24)
     }
     ]

for list in list_rw:
    x = list['arrival'] - list['departure']
    print(x)
    if x < datetime.time(7, 30):
        new_list.append(list)


# print(new_list)
