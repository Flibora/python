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

count = 0
flag = True
for i in range(1,n):
    if list_n[i-1] < list_n[i] :
        if flag:
            count += 1
            flag = False
    else :
        flag = True
print(count)
