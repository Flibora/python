#Дан список целых чисел. Подсчитать сколько четных
#чисел в списке

list_num = [2, 4, 6, 5, 7, 10]
summa = 0
for i in list_num:
    if not i % 2:
        summa += 1
print(summa)
