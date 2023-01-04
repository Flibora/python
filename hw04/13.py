# Дан список. Создать новы список, сдвинуты на 1
# элемент влево Пример:12345 -> 23451

spisok_a = [2, 4, 6, 4, 5]

spisok_b = [None] * 5
lenght_a = len(spisok_a)

i = 0
while i < lenght_a:
    spisok_b[i-1] = spisok_a[i]
    i += 1
print(spisok_b)
