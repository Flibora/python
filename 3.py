#Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar':
#'usd', 'ruble': 'rub'}
#Добавить каждому ключу число равное длине этого
#ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
#получить список ключе - использовать метод .keys()
#(подсказка: создается новы ключ с цифро в конце,
#стары удаляется)


dict_a = {'test': 'test_value', 'europe': 'eur', 'dollar':
'usd', 'ruble': 'rub'}
list_key = list(dict_a.keys())

for key in list_key:
    new_key = f'{key}{len(key)}'
    dict_a[new_key] = dict_a.pop(key)

print(dict_a)
