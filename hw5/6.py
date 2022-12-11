# Задан целочисленны список c n случайных
# элементов. Определить количество участков списка,
# на котором элементы монотонно возрастают (каждое
# следующее число больше предыдущего).
import random

sum = 0
list_n = []
n = int(input())

for i in range(n):
    chislo = random.randrange(0, 100)
    list_n.append(chislo)

print(list_n)

for i in range(n):
    if i == n - 1:
        break
    elif list_n[i] < list_n[i+1]:
        sum +=1

print(sum)
