'''Дан список целых чисел. Создать новы список, кажды элемент которого равен
исходному элементу умноженному на -2'''


a = [1, 2, 3, 4, 5]
lenght = len(a)
new_a = []
i = 0
while  i < lenght:
    new_a.append(a[i] * -2)
    i += 1
print(new_a)
