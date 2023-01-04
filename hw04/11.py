# Дан список целых чисел. Подсчитать сколько четных
# чисел в списке

a = [1, 2, 3, 4, 5, 6]
lenght = len(a)
i = 0
summa = 0
while i < lenght:
    if a[i] % 2 == 0:
        summa += a[i]
    i += 1
print(summa)
