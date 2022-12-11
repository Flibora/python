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

spisok.sort(reverse=True)
print(spisok)

for j in range(len(spisok)):
    if not spisok[j] % 2:
        spisok[j] = spisok[0]

print(spisok)
