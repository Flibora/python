# В списке целых случайных чисел с количеством
# элементов n определить максимальное число и
# заменить им все четные по значению элементы.
import random

spisok = []

n = int(input())

for i in range(n):
    #num = random.randint(0 , 99)
    spisok.append(random.randint(0 , 99))

print(spisok)

# spisok.sort(reverse=True)
# print(spisok)
max_el = 0
for i in spisok:
    if i > max_el:
        max_el = i

print(max_el)

for j in range(len(spisok)):
    if not spisok[j] % 2:
        spisok[j] = max_el

print(spisok)
