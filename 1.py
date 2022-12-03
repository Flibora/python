#Дан список целых чисел.
#Создать новы список, кажды элемент которого равен
#исходному элементу умноженному на -2

list_num = [2, 4, 6, 5, 7, 10]
new_list_num = []
for i in list_num:
    i *= -2
    new_list_num.append(i)
print(new_list_num)
