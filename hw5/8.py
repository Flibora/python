# В заданно строке расположить в обратном порядке
# все слова. Разделителями слов считаются пробелы.

stroka = str('В заданно строке расположить в обратном порядке все слова')

print(stroka)
new_stroka = stroka.split()
new_stroka.reverse()
print(' '.join(new_stroka))
