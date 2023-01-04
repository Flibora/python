'''Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar':
'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого
ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}). Чтобы
получить список ключе - использовать метод .keys()
(подсказка: создается новы ключ с цифро в конце,
стары удаляется)'''


dict_a = {'test': 'test_value', 'europe': 'eur', 'dollar':
'usd', 'ruble': 'rub'}
kolichestvo= len(dict_a.keys())
list_key = list(dict_a.keys())
i = 0
while i < kolichestvo:
    dlina_key = str(len(list_key[i]))
    new_key = list_key[i] + dlina_key
    dict_a[new_key] = dict_a[list_key[i]]
    del dict_a[list_key[i]]
    i += 1

print(dict_a)
