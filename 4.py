#Дан список. Создать новы список, сдвинуты на 1
#элемент влево Пример:12345 -> 23451

list_num = [1, 2, 3, 4, 5]
new_list = []

for i in range(len(list_num)):
    if i + 1 == len(list_num):
        new_list.append(list_num[0])
    else: new_list.append(list_num[i+1])

print(new_list)
